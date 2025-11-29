def to_snake_case(key):
    key = key.strip().replace(" ", "_").replace("-", "_")
    result = ""

    for i, char in enumerate(key):
        if char.isupper():
            if i != 0:
                prev = key[i - 1]
                if prev.islower():
                    result += "_"
        result += char.lower()

    return result


def transform_rows(row):
    transformed = {}
    for key, value in row.items():
        new_key = to_snake_case(key)
        value = value.strip()
        if "/" in value:
            parts = value.split("/")
            if(len(parts) == 3 and all(p.isdigit() for p in parts)):
                mm, dd, yyyy = parts
                value = f"{yyyy}-{mm.zfill(2)}-{dd.zfill(2)}"
        if "@" in value and " " in value:
            value = value.replace(" ", "")
        
        if new_key == "full_name":
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            
            value = " ".join(value.split())

            value = value.replace("-", " ")

        transformed[new_key] = value

    return transformed

def transform_csv(rows):
    print("Transforming data...")
    transformed_rows = []
    for row in rows:
        transformed_rows.append(transform_rows(row))

    print("Data transformed successfully.")
    return transformed_rows
