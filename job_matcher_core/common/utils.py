import csv

def load_items_from_df(Type, df):
    # Here we convert the dataframe chunk into a list of lists:
    df_rows = [[str(i) for i in row] for row in df.itertuples()]
    items = []
    for df_row in df_rows:
        row = df_row[1:]
        row_no = int(df_row[0])
        items.append(Type(row, row_no + 1))
    return items


def load_items_from_csv(Type, csv_path = None):
    items = []
    path = csv_path if csv_path else Type.csv_path
    with open(path) as file_obj:
        # skip the header:
        next(file_obj) 
        for row_no, row in enumerate(csv.reader(file_obj, skipinitialspace=True)):
            items.append(Type(row, row_no + 1))
    return items
