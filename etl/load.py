import pyodbc

def load_to_sql_server(rows):
    print("Loading data to SQL Server...")
    conn_str = (
        "Driver={SQL Server};"
        "Server=localhost\\SQLEXPRESS;" 
        "Database=CustomerETL;"
        "Trusted_Connection=yes;"
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    insert_sql = """
        INSERT INTO Customers (FullName, Age, RegistrationDate, Email, UserId)
        VALUES (?, ?, ?, ?, ?)
    """

    for row in rows:
        full_name = row.get("full_name")
        age = row.get("age")
        reg_date = row.get("registration_date")
        email = row.get("email")
        user_id = row.get("user_id")

        # konverzija tipova
        age_val = int(age) if age is not None and age != "" else None

        cursor.execute(
            insert_sql,
            full_name,
            age_val,
            reg_date,  # string "YYYY-MM-DD" je OK za DATE kolonu u SQL-u
            email,
            user_id
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("Data loaded successfully.")
