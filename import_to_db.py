"""
Import data from data/superstore_sales.csv into a local PostgreSQL database.
"""

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


def main() -> None:
    project_root = Path(__file__).resolve().parent
    csv_path = project_root / "data" / "superstore_sales.csv"

    if not csv_path.exists():
        print(f"CSV file not found at {csv_path}")
        return

    try:
        df = pd.read_csv(csv_path)
    except Exception as exc:
        print("Failed to read CSV file.")
        print(f"Error: {exc}")
        return

    db_url = "postgresql+psycopg2://postgres:password@localhost/postgres"

    try:
        engine = create_engine(db_url)
        with engine.begin() as conn:
            # Ensure table exists fresh (replace if it already exists)
            conn.execute(text("DROP TABLE IF EXISTS sales_data"))
            df.to_sql("sales_data", conn, if_exists="replace", index=False)
    except SQLAlchemyError as exc:
        print("Failed to connect to the PostgreSQL database or import data.")
        print(f"Error: {exc}")
        return

    print("Data imported successfully!")


if __name__ == "__main__":
    main()

