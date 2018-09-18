# circleci_python_helpers
Simple Python scripts for CircleCI

* `set_circleci_env_variable.py` - set environment variables in CircleCI through code
* `trigger_circleci_job.py` - triggers a job in circleci with temporary environment variables that exist for the duration of the job


## Usage


### Setting one environment variable

``` bash
export GITHUB_OWNER=<YOUR GITHUB ORG NAME OR USERNAME>
export GITHUB_REPO=<YOUR GITHUB REPO NAME>
export CIRCLECI_TOKEN=<YOUR CIRCLECI TOKEN>
./set_circleci_env_variable.py --key "TEST_KEY" --value "TEST_VALUE"
```

### Setting environment data from a file

```
export GITHUB_OWNER=<YOUR GITHUB ORG NAME OR USERNAME>
export GITHUB_REPO=<YOUR GITHUB REPO NAME>
export CIRCLECI_TOKEN=<YOUR CIRCLECI TOKEN>
./set_circleci_env_variable.py --key "TEST_KEY" --value "$(cat YOUR_FILE_PATH)"
```

### Setting multiple environment variables

``` bash
export GITHUB_OWNER=<YOUR GITHUB ORG NAME OR USERNAME>
export GITHUB_REPO=<YOUR GITHUB REPO NAME>
export CIRCLECI_TOKEN=<YOUR CIRCLECI TOKEN>
./set_circleci_env_variable.py --key "TEST_KEY_01" --value "TEST_VALUE_01"
./set_circleci_env_variable.py --key "TEST_KEY_02" --value "TEST_VALUE_01"
```

### Triggering a job in CircleCI with one-off environment variables

``` bash
export GITHUB_OWNER=<YOUR GITHUB ORG NAME OR USERNAME>
export GITHUB_REPO=<YOUR GITHUB REPO NAME>
export CIRCLECI_TOKEN=<YOUR CIRCLECI TOKEN>
export CIRCLECI_JOB_ENV_EXAMPLE1="Test 1"
export CIRCLECI_JOB_ENV_EXAMPLE2="Test 2"
./trigger_circleci_job.py --repo "<YOUR GITHUB REPO HERE>" --branch "<YOUR GITHUB BRANCH HERE>" --circle-job "<YOUR CIRCLECI JOB NAME HERE>"
```