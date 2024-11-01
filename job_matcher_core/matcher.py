from job_matcher_core.classes.jobseeker import JobSeeker
from job_matcher_core.classes.job import Job
from job_matcher_core.common.utils import load_items_from_csv, load_items_from_df, get_input_paths
import pandas as pd

def match_optimisation_01():

    jobseekers_csv_path, jobs_csv_path = get_input_paths() 

    jobs = load_items_from_csv(Job, jobs_csv_path)

    # In this method we use pandas to load the jobseeker.csv file in chunks, to better handle large inputs:
    df_iter = pd.read_csv(jobseekers_csv_path, iterator=True, chunksize=5)
    while True: 
        try:
            # Load a chunk of data into the dataframe:
            df = next(df_iter)
            # print(f'Another chunk \n {df}')
            jobseekers = load_items_from_df(JobSeeker, df)
        except StopIteration:
            # print('Data ingestion completed.')
            break

        matched_and_sorted = match_and_sort(jobseekers, jobs)
        match_display(matched_and_sorted)


def match_and_sort(jobseekers, jobs):

    matched = []

    for jobseeker in jobseekers:
        for job in jobs:
            matching = jobseeker.skills.intersection(job.required_skills)
            matching_skill_count = len(matching)
            matching_skill_percent = (matching_skill_count / len(job.required_skills)) * 100

            if matching_skill_percent:
                matched.append({
                    'jobseeker_id': jobseeker.id,
                    'jobseeker_name': jobseeker.name,
                    'job_id': job.id, 
                    'job_title': job.title, 
                    'matching_skill_count': matching_skill_count, 
                    'matching_skill_percent': matching_skill_percent
                })

    return sorted(matched, key=lambda x: (
        x['jobseeker_id'],
        -x['matching_skill_percent'],
        x['job_id']))


def match_display(matched_and_sorted):
    for item in matched_and_sorted:
        print(f'{item['jobseeker_id']}, {item['jobseeker_name']}, {item['job_id']}, {item['job_title']}, {item['matching_skill_count']}, {round(item['matching_skill_percent'])}')
            

def match_naive():
    jobseekers = load_items_from_csv(JobSeeker)
    jobs = load_items_from_csv(Job)
    matched_and_sorted = match_and_sort(jobseekers, jobs)
    match_display(matched_and_sorted)


