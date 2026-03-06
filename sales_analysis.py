"""
Run SQL-based sales analysis on the sales_data table.

Query 1: Total Sales and Profit by Category (descending by Sales).
Query 2: Top 3 Sub-Categories with lowest total Profit (ascending by Profit).
"""

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def main() -> None:
    db_url = "postgresql+psycopg2://postgres:password@localhost/postgres"

    try:
        engine = create_engine(db_url)
    except SQLAlchemyError as exc:
        print("Failed to create database engine.")
        print(f"Error: {exc}")
        return

    try:
        # Query 1: Top performers by Category
        query_top_performers = """
            SELECT
                "Category" AS category,
                SUM("Sales") AS total_sales,
                SUM("Profit") AS total_profit
            FROM sales_data
            GROUP BY "Category"
            ORDER BY total_sales DESC;
        """
        df_top_perf = pd.read_sql(query_top_performers, con=engine)

        # Query 2: Loss leaders by Sub-Category
        query_loss_leaders = """
            SELECT
                "Sub-Category" AS sub_category,
                SUM("Profit") AS total_profit
            FROM sales_data
            GROUP BY "Sub-Category"
            ORDER BY total_profit ASC
            LIMIT 3;
        """
        df_loss_leaders = pd.read_sql(query_loss_leaders, con=engine)
    except SQLAlchemyError as exc:
        print("Failed to run analysis queries.")
        print(f"Error: {exc}")
        return

    print("=== Top Performers by Category ===")
    print(df_top_perf.to_string(index=False))
    print("\n=== Loss Leaders (Top 3 Sub-Categories by Lowest Total Profit) ===")
    print(df_loss_leaders.to_string(index=False))


if __name__ == "__main__":
    main()

