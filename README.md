# Job Matcher

This is a simple POC that matches job seekers to jobs.

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
source .venv/bin/activate
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
 Name the two `.csv` files `jobseekers.csv` & `jobs.csv` and drop them into `./job_matcher_core/data`. Then:
```
python main.py
```
## Run the tests
```
python -m unittest job_matcher_core/test/main.py
```
## TODO:
- More unit tests
- Improving the efficiency: Currently I'm loading all the jobseekers & all the jobs and then doing the match. My next step was to first load all the jobs, then calculate the best match for each jobseeker, one at a time.

