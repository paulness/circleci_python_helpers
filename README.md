# set-circleci-env-variables
Simple Python script to set environment variables in CircleCI through code.

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