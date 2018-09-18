#!/usr/bin/env python3
"""
Deletes all the saved environment variables in CircleCI via their v1.1 API interface
"""

import argparse
import os
import requests
import json
import sys
import urllib


class CircleCiEnvVarDeleter():

    def __init__(self, circle_token, github_owner, github_repo):
        self.circle_token = circle_token
        self.github_owner = github_owner
        self.github_repo = github_repo


    def delete_all_circleci_env_variables(self):
        keys_to_delete = self._get_circleci_env_variables()
        for key in keys_to_delete:
            print('Deleting key: %s' % key)
            self._delete_circleci_env_variable(key)


    def _get_circleci_env_variables(self):
        """Gets all the circleci environment variables currently set in a project"""
        url = "https://circleci.com/api/v1.1/project/github/%s/%s/envvar?circle-token=%s" % (self.github_owner, self.github_repo, self.circle_token)
        response = requests.get(url)
        keys = []
        for kvp in response.json():
            keys.append(kvp['name'])
        return keys


    def _delete_circleci_env_variable(self, key):
        """Deletes a circleci env variable"""

        url = "https://circleci.com/api/v1.1/project/github/%s/%s/envvar/%s?circle-token=%s" % (self.github_owner, self.github_repo, urllib.parse.quote_plus(key), self.circle_token)
        response = requests.delete(url)
        response.raise_for_status()


def main():
    """Deletes all circleci environment variables for a project from the CLI"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--circle-token', required=True)
    parser.add_argument('--github-owner', required=True)
    parser.add_argument('--github-repo', required=True)
    args = parser.parse_args()

    CircleCiEnvVarDeleter(args.circle_token, args.github_owner, args.github_repo).delete_all_circleci_env_variables()


if __name__ == "__main__":
    main()
