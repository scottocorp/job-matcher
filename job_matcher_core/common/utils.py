from job_matcher_core.classes.jobseeker import JobSeeker
from job_matcher_core.classes.job import Job
import csv
from pathlib import Path

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


def get_input_path(Type, command_string):
    csv_path = input(command_string)

    if not csv_path:
        csv_path = Type.csv_path
    else:
        csv_path = Path(csv_path)
        if not csv_path.exists():
            raise Exception(f'ERROR: {csv_path} does not exist.')
        if not csv_path.is_file():
            raise Exception(f'ERROR: {csv_path} is not a file.')

    return csv_path


def get_input_paths():
    jobseekers_csv_path = get_input_path(JobSeeker, f'Please enter the jobseekers .csv path (default is job_matcher/data/jobseekers.csv): ')
    jobs_csv_path = get_input_path(Job, f'Please enter the jobs .csv path (default is job_matcher/data/jobs.csv): ')

    return (jobseekers_csv_path, jobs_csv_path)
