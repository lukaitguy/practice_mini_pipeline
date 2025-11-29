def read_csv_custom(path):
    rows = []
    with open(path, 'r') as file:
        print("Reading CSV file:", path)
        headers = file.readline().strip().split(',')

        for line in file:
            values = line.strip().split(',')
            row = {}

            for h, v in zip(headers, values):
                row[h] = v.strip()

            rows.append(row)

    return rows