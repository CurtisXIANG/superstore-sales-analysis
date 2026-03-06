"""
Visualize sales performance from the sales_data table.

Left:  Bar chart of total Sales by Category.
Right: Line chart of monthly Sales trend.
Saves figure as sales_dashboard.png in the project root.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def load_data():
    db_url = "postgresql+psycopg2://postgres:password@localhost/postgres"
    engine = create_engine(db_url)

    # Total sales by Category
    query_category = """
        SELECT
            "Category" AS category,
            SUM("Sales") AS total_sales
        FROM sales_data
        GROUP BY "Category"
        ORDER BY total_sales DESC;
    """

    # Total sales by Month (based on Order Date)
    query_monthly = """
        SELECT
            DATE_TRUNC('month', "Order Date"::date) AS order_month,
            SUM("Sales") AS total_sales
        FROM sales_data
        GROUP BY order_month
        ORDER BY order_month;
    """

    df_category = pd.read_sql(query_category, con=engine)
    df_monthly = pd.read_sql(query_monthly, con=engine)

    # Ensure naive datetime (drop timezone if present) for plotting
    if getattr(df_monthly["order_month"].dtype, "tz", None) is not None:
        df_monthly["order_month"] = df_monthly["order_month"].dt.tz_localize(None)

    return df_category, df_monthly


def create_plots(df_category: pd.DataFrame, df_monthly: pd.DataFrame, output_path: Path) -> None:
    plt.style.use("seaborn-v0_8")

    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Sales by Category (bar chart)
    ax_left.bar(df_category["category"], df_category["total_sales"], color="#4C72B0")
    ax_left.set_title("Total Sales by Category")
    ax_left.set_xlabel("Category")
    ax_left.set_ylabel("Total Sales")
    ax_left.tick_params(axis="x", rotation=30)

    # Right: Monthly Sales Trend (line chart)
    ax_right.plot(
        df_monthly["order_month"],
        df_monthly["total_sales"],
        marker="o",
        color="#DD8452",
    )
    ax_right.set_title("Monthly Sales Trend")
    ax_right.set_xlabel("Month")
    ax_right.set_ylabel("Total Sales")
    ax_right.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def main() -> None:
    try:
        df_category, df_monthly = load_data()
    except SQLAlchemyError as exc:
        print("Failed to load data from PostgreSQL.")
        print(f"Error: {exc}")
        return

    project_root = Path(__file__).resolve().parent
    output_path = project_root / "sales_dashboard.png"

    create_plots(df_category, df_monthly, output_path)
    print(f"Dashboard image saved to: {output_path}")


if __name__ == "__main__":
    main()

