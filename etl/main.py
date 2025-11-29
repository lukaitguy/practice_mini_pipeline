import transform
import load
import extract

def main():
    # EXTRACT
    rows = extract.read_csv_custom("../data/customers.csv")

    # TRANSFORM
    cleaned_rows = transform.transform_csv(rows)
    
    # LOAD
    load.load_to_sql_server(cleaned_rows)

if __name__ == "__main__":
    main()