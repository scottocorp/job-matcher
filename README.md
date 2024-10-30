# Job Matcher

This is a simple POC that matches job seekers to jobs.

Example snippet from the inputted **job seekers** `.csv`:
```
id,name,skills
1,Jane Doe,"Ruby, SQL, Problem Solving"
2,John Smith,"JavaScript, HTML/CSS, Teamwork"
3,Ann Coder,"Java, SQL, Problem Solving"
...
```
Example snippet from the inputted **jobs** `.csv`:
```
id,title,required_skills
1,Ruby Developer,"Ruby, SQL, Problem Solving"
2,Frontend Developer,"JavaScript, HTML/CSS, React, Teamwork"
3,Backend Developer,"Java, SQL, Node.js, Problem Solving"
...
```
After running the code, the output would be:
```
1, Jane Doe , 1, Ruby Developer, 3, 100
1, Jane Doe, 3, Backend Developer, 2, 50
2, John Smith, 2, Frontend Developer, 3, 75
3, Anne Coder, 3, Backend Developer, 3, 75
3, Anne Coder, 1, Ruby Developer, 2, 67
...
```
Ie: For each job seeker, the jobs are ranked in terms of which is the best match. So for example, there is a 100% match between the Jane's skills and the skills required for a Ruby Developer.

The outputted fields correspond to:

**jobseeker_id, jobseeker_name, job_id, job_title, matching_skill_count, matching_skill_percent**

## Setup

### Install Python

You'll need to install python. I use [conda](https://anaconda.org/anaconda/conda) to switch between different versions. I used version `3.13.0`.

### Clone the Repository

```
git clone git@github.com:scottocorp/job-matcher.git
cd job-matcher
```

### Install the Virtual Environment

1. Create a virtual environment in a folder called `.venv`:

```
python -m venv .venv
```

2. Activate the virtual environment:

```
# Linux or Mac:
source .venv/bin/activate
# Windows:
source .venv/Scripts/activate
```
3. Deactivate the virtual environment:

```
deactivate
```
### Install the Packages

```
pip install -r requirements.txt
```
## Run the code
```
python main.py
```
... and enter the paths to the job seekers `.csv` & the jobs `.csv`.
## Run the tests
```
python -m unittest job_matcher_core/test/main.py
```
## TODO:
- More unit tests
- Improving the efficiency: I've updated the repo by using Pandas to better handle large inputs.

