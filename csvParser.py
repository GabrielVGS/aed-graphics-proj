class CSVParser:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        return [line.strip().split(',') for line in lines]

    def __getitem__(self, key):
        if isinstance(key, int):  # Access by row index
            if 0 <= key < len(self.data):
                return CSVRow(self, key)
            else:
                raise IndexError("Index out of range")

        elif isinstance(key, str):  # Access by column name
            if len(self.data) == 0:
                return []
            
            headers = self.data[0]
            if key in headers:
                key_index = headers.index(key)
                return CSVColumn(self, key_index)
            else:
                raise KeyError(f"Column '{key}' not found")

        else:
            raise TypeError("Key must be an integer or a string")

    def __len__(self):
        return len(self.data)

    def write_csv(self, new_data):
        with open(self.filename, 'w') as file:
            for row in new_data:
                file.write(','.join(row) + '\n')
    def find_user_index(self, username):
        if len(self.data) == 0:
            return None
        
        headers = self.data[0]
        if "usuario" in headers:
            user_index = headers.index("usuario")
            for i, row in enumerate(self.data[1:], start=1):
                if row[user_index] == username:
                    return i
        return None

class CSVRow:
    def __init__(self, csv_parser, row_index):
        self.csv_parser = csv_parser
        self.row_index = row_index

    def __getitem__(self, key):
        if isinstance(key, str):  # Access by column name
            return self.csv_parser.data[self.row_index + 1][self.csv_parser[key]]

        elif isinstance(key, int):  # Access by column index
            return self.csv_parser.data[self.row_index + 1][key]

        else:
            raise TypeError("Key must be an integer or a string")

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.csv_parser.data[self.row_index + 1][self.csv_parser[key]] = value
            self.csv_parser.write_csv(self.csv_parser.data)
        elif isinstance(key, int):
            self.csv_parser.data[self.row_index + 1][key] = value
            self.csv_parser.write_csv(self.csv_parser.data)
        else:
            raise TypeError("Key must be an integer or a string")

class CSVColumn:
    def __init__(self, csv_parser, column_index):
        self.csv_parser = csv_parser
        self.column_index = column_index

    def __getitem__(self, key):
        if isinstance(key, int):  # Access by row index
            return self.csv_parser.data[key + 1][self.column_index]
        else:
            raise TypeError("Key must be an integer")

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.csv_parser.data[key + 1][self.column_index] = value
            self.csv_parser.write_csv(self.csv_parser.data)
        else:
            raise TypeError("Key must be an integer")

