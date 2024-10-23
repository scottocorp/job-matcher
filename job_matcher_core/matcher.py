from job_matcher_core.classes.jobseeker import JobSeeker
from job_matcher_core.classes.job import Job
from job_matcher_core.common.utils import load_items


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
    jobseekers = load_items(JobSeeker)
    jobs = load_items(Job)
    matched_and_sorted = match_and_sort(jobseekers, jobs)
    match_display(matched_and_sorted)


