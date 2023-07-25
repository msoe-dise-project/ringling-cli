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
import requests
from requests.exceptions import ConnectionError as RequestsConnectionError
from .response_handling import handle_create
from .response_handling import handle_get
from .response_handling import perform_list


def get_url(base_url):
    """
    Get the URL for interacting with projects
    :return: The project URL
    """
    return base_url + "/v1/model_tests"


def create_model_test(base_url, obj):
    """
    Create a model test on the Ringling service
    :param base_url: The URL of the Ringling Service
    :param obj: The model object payload
    :return: None
    """
    try:
        response = requests.post(get_url(base_url),
                                 json=obj, timeout=5)
        if handle_create(response):
            print(f"Model Test created with ID {response.json()['test_id']}")
    except RequestsConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)


def get_model_test(base_url, trained_model_id):
    """
    Get a model test given an ID
    :param base_url: The URL of the Ringling Service
    :param trained_model_id: The ID of the model test
    :return: None
    """
    url = get_url(base_url) + "/" + str(trained_model_id)
    try:
        response = requests.get(url, timeout=5)
        handle_get(response, "Model Test", trained_model_id)
    except RequestsConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)


def list_model_tests(base_url):
    """
    List all the model tests in the Ringling Service
    :param base_url: The URL of the Ringling Service
    :return: None
    """
    perform_list(get_url(base_url))
