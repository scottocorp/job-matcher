import unittest
from os import path
import json
from job_matcher_core.classes.jobseeker import JobSeeker
from job_matcher_core.classes.job import Job
from job_matcher_core.common.utils import load_items_from_csv
from job_matcher_core import matcher


def match_test():
    base_path = path.dirname(__file__)    
    jobseekers_test = load_items_from_csv(JobSeeker, f'{base_path}/jobseekers.csv')
    jobs_test = load_items_from_csv(Job, f'{base_path}/jobs.csv')
    return matcher.match_and_sort(jobseekers_test, jobs_test)


class TestJobMatcherMethods(unittest.TestCase):

    def test_extracted(self):

        matched_and_sorted_actual = json.dumps(match_test())

        # Given the test input above we expect to see the job list to be sorted in this order: job id=1, job id=3, job id=2
        # The json representation of this sorted list is below:
        matched_and_sorted_expected = '[{"jobseeker_id": 1, "jobseeker_name": "Alice Seeker", "job_id": 1, "job_title": "Ruby Developer", "matching_skill_count": 3, "matching_skill_percent": 100.0}, {"jobseeker_id": 1, "jobseeker_name": "Alice Seeker", "job_id": 3, "job_title": "Python Developer", "matching_skill_count": 2, "matching_skill_percent": 50.0}, {"jobseeker_id": 1, "jobseeker_name": "Alice Seeker", "job_id": 2, "job_title": "Backend Developer", "matching_skill_count": 1, "matching_skill_percent": 33.33333333333333}]'

        self.assertEqual(matched_and_sorted_actual, matched_and_sorted_expected)


if __name__ == '__main__':
    unittest.main()
