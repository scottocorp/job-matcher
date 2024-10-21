import csv

def load_items(Type, csv_path = None):
    items = []
    path = csv_path if csv_path else Type.csv_path
    with open(path) as file_obj:
        # skip the header:
        next(file_obj) 
        for row_no, row in enumerate(csv.reader(file_obj, skipinitialspace=True)):
            items.append(Type(row, row_no + 1))
    return items
