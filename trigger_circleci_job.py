#!/usr/bin/env python3
"""
Triggers an ad-hoc job in CircleCI with temporary environment variables set, via their v1.1 API
"""

import argparse
import os
import requests
import json
import sys
import urllib


def trigger_circleci_build(job_args, github_owner, github_repo, git_branch, circle_token):
    """Triggers a CircleCI job with temporary environment variables"""

    url = "https://circleci.com/api/v1.1/project/github/%s/%s/tree/%s?circle-token=%s" % (github_owner, github_repo, urllib.parse.quote_plus(git_branch), circle_token)
    payload = { 'build_parameters': job_args }

    response = requests.post(url, json=payload)
    response.raise_for_status()


def main():
    """Triggers a CircleCI job from the CLI"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', required=True)
    parser.add_argument('--branch', required=True)
    parser.add_argument('--circle-job', required=True)
    args = parser.parse_args()
    github_owner=os.environ['GITHUB_OWNER']
    circle_token=os.environ['CIRCLECI_TOKEN']

    job_args = {}
    for key in os.environ:
        if key.startswith("CIRCLECI_JOB_ENV_"):
            job_args[key] = os.environ[key]

    job_args['CIRCLE_JOB'] = args.circle_job
    trigger_circleci_build(job_args, github_owner, args.repo, args.branch, circle_token)


if __name__ == "__main__":
    main()
