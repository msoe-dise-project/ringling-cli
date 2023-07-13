"""
Copyright 2023 MSOE DISE Project

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import pprint
import requests
from requests.exceptions import ConnectionError

def handle_create(response):
    """
    Handle the response from create commands
    :param response: the response object
    :return: if the response was a success
    """
    if 200 <= response.status_code < 300:
        return True
    if response.status_code == 400:
        print(response.json()['error'], file=sys.stderr)
        sys.exit(1)
    return False


def handle_modify(response, object_type, cur_id):
    """
    Handle the response from modify commands
    :param response: the response object
    :param object_type: the object type (for displaying errors)
    :param cur_id: the id of the object
    :return: if the response was a success
    """
    if 200 <= response.status_code < 300:
        return True
    if response.status_code == 404:
        print(f"Invalid {object_type} ID {cur_id}", file=sys.stderr)
        sys.exit(1)
    if response.status_code == 400:
        print(response.json()['error'], file=sys.stderr)
        sys.exit(1)
    return False


def handle_get(response, object_type, cur_id):
    """
    Handle the response from get commands
    :param response: the response object
    :param object_type: the object type (for displaying errors)
    :param cur_id: the id of the object
    :return: if the response was a success
    """
    if 200 <= response.status_code < 300:
        return True
    if response.status_code == 404:
        print(f"Invalid {object_type} ID {cur_id}", file=sys.stderr)
        sys.exit(1)
    return False


def perform_list(endpoint_url):
    try:
        response = requests.get(endpoint_url, timeout=5)
        response_json = response.json()
        pprint.pprint(response_json)
    except ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)