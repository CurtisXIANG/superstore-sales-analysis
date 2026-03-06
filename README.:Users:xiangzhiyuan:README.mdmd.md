Superstore Sales Analysis
=========================

### Project overview

This is a **vibe coding** data project, built iteratively through natural-language prompts rather than a fixed upfront spec.  
The goal is to simulate a Global Superstore dataset, load it into PostgreSQL, and then explore it with SQL, Python, and visualizations.

### Prompt-driven workflow

You guided the project step by step with prompts. In simplified form, the key prompts were:

- **Project setup**
  - Create a `data/` folder.
  - Create `README.md` with the title *Superstore Sales Analysis*.
  - Add a Python-style `.gitignore`.

- **Data generation**
  - Create `generate_data.py` to generate a synthetic Global Superstore-style CSV (`data/superstore_sales.csv`) with 500 rows and the columns:
    - `Order ID`, `Order Date`, `Customer Name`, `Segment`, `City`, `State`, `Country`,
      `Product Name`, `Category`, `Sub-Category`, `Sales`, `Quantity`, `Profit`.
  - Run the script and ensure the CSV is created.

- **Environment and dependencies**
  - When a script failed due to missing libraries, create `requirements.txt`, add needed packages (e.g. `pandas`, `SQLAlchemy`, `psycopg2-binary`, `matplotlib`), and run:
    - `pip install -r requirements.txt`

- **Database import and verification**
  - Create `import_to_db.py` to:
    - Read the CSV with `pandas`.
    - Connect to the local PostgreSQL database (`postgres` / `postgres` / `password` on `localhost`).
    - Create (or replace) a `sales_data` table and import the CSV data.
    - Print `Data imported successfully!` when done.
  - Create `verify_data.py` to:
    - Run `SELECT * FROM sales_data LIMIT 5;` and print the first 5 rows.
    - Run `SELECT COUNT(*) FROM sales_data;` and print the total row count.

- **SQL analysis with pandas**
  - Create `sales_analysis.py` to run two SQL-based analyses via `pandas.read_sql`:
    1. **Top performers**: total `Sales` and `Profit` by `Category`, ordered by total Sales (descending).
    2. **Loss leaders**: top 3 `Sub-Category` values with the lowest total `Profit`, ordered ascending.
  - Print both result tables clearly to the terminal.

- **Visualization**
  - Create `visualize_data.py` to:
    - Query total Sales by `Category`.
    - Query total Sales by month (derived from `Order Date`).
    - Produce a **dashboard image** with:
      - Left: bar chart of Sales by Category.
      - Right: line chart of Monthly Sales Trend.
    - Save the combined figure as `sales_dashboard.png`.

### What has been achieved

- **Synthetic dataset created**
  - `generate_data.py` produces `data/superstore_sales.csv` with 500 realistic synthetic orders and all required fields.

- **Database pipeline working end-to-end**
  - `import_to_db.py` loads the CSV into a local PostgreSQL database table named `sales_data`.
  - `verify_data.py` confirms the structure and row count (`500` rows) directly from the database.

- **Analytical insights via SQL + pandas**
  - `sales_analysis.py` computes:
    - Total Sales and Profit per `Category` (top performers).
    - The `Sub-Category` entries with the weakest overall Profit (loss leaders).

- **Visual dashboard**
  - `visualize_data.py` generates `sales_dashboard.png`, combining:
    - A bar chart of Sales by Category.
    - A line chart showing the monthly Sales trend over time.

Together, these pieces form a small but complete vibe-coded analytics stack:
data generation → database import → SQL + pandas analysis → visual dashboard.

