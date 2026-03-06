"""
Verify data in the sales_data table of the local PostgreSQL database.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


def main() -> None:
    db_url = "postgresql+psycopg2://postgres:password@localhost/postgres"

    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            # Fetch first 5 rows
            result = conn.execute(text("SELECT * FROM sales_data LIMIT 6;"))
            rows = result.fetchall()

            print("First 5 rows from sales_data:")
            for row in rows:
                print(dict(row._mapping))

            # Count total rows
            count_result = conn.execute(text("SELECT COUNT(*) AS total_rows FROM sales_data;"))
            total_rows = count_result.scalar_one()
            print(f"\nTotal number of rows in sales_data: {total_rows}")

    except SQLAlchemyError as exc:
        print("Failed to connect to the PostgreSQL database or run queries.")
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

