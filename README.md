# Mini ETL Pipeline: CSV -> Python -> SQL Server

This is mini ETL project which demonstrate complete process:
Extract->Transform->Load
implemented entirely in Python using a custom CSV parser and SQL Server

# Features
- Custom CSV parser
- CamelCase / PascalCase / MixedCase -> snake_case conversion
- Data cleaning
- Date conversion
- Parsing and cleaning email
- SQL Server table + INSERT with pyodbc
- Modular structure: extract, transform, load

# Folder Structure
```
project-root/
│
├── data/
│   ├── customers.csv
│   └── ddl_script.sql
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
└── README.md
```

# Tech Stack
- Python
- SQL Server
- ETL without libraries

# 1. Extract (CSV Parsing)
The read_csv_custom() function:
  - reads the header
  - maps each row to a dictionary
  - strips unnecessary whitespace

# 2. Transform (Data Cleaning & Normalization)
Transform includes:
  - converting all keys to snake_case
  - cleaning names
  - converting dates
  - cleaning and normalizing email addresses

# 3. Load (SQL Server)
Table schema:
```sql
CREATE TABLE Customers (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FullName NVARCHAR(100),
    Age INT NULL,
    RegistrationDate DATE NULL,
    Email NVARCHAR(255),
    UserId NVARCHAR(50)
);
```
Python loader:
```python
load_to_sql_server(cleaned_rows)
```
The project uses pyodbc for database communication:
```python
conn_str = (
    "Driver={SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=CustomerETL;"
    "Trusted_Connection=yes;"
)
```

# How to run the Pipeline
```python
python etl/main.py
```

main.py orchestrates the pipeline:
  - extract from CSV
  - transform raw data
  - load into SQL Server

# Future improvements

This is a little project that helps me better understand data pipelines and working with python.
A few improvements I will add to this project:
- Logging module
- Error handling
- ...

If you have any suggestion what to improve or what to add, feel free to reach me out!


