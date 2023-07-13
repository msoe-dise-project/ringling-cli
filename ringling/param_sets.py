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
from .response_handling import handle_create
from .response_handling import handle_get
from .response_handling import handle_modify
from .response_handling import perform_list

def get_url(base_url):
    """
    Get the URL for interacting with projects
    :return: The project URL
    """
    return base_url + "/v1/parameter_sets"


def create_param_set(base_url, project_id, training_params, is_active):
    """
    Create a parameter set on the Ringling service
    :param base_url: The URL of the Ringling Service
    :param project_id: The ID of the project that the parameter set belongs to
    :param training_params: The parameters of the parameter set
    :param is_active: If the parameter set is active or inactive
    :return: None
    """
    obj = {"project_id": project_id,
           "training_parameters": training_params,
           "is_active": is_active}

    try:
        response = requests.post(get_url(base_url),
                                 json=obj, timeout=5)
        if handle_create(response):
            response_json = response.json()
            print(f"Parameter Set created successfully with ID {response_json['parameter_set_id']}")
    except ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)

def get_param_set(base_url, param_set_id):
    """

    :param base_url: The URL of the Ringling Service
    :param param_set_id: The ID of the parameter set
    :return: None
    """
    url = get_url(base_url) + "/" + str(param_set_id)
    try:
        response = requests.get(url, timeout=5)
        if handle_get(response, "Parameter Set", param_set_id):
            response_json = response.json()
            pprint.pprint(response_json)
    except ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)


def modify_param_set(base_url, param_set_id, is_active):
    """

    :param base_url: The URL of the Ringling Service
    :param param_set_id: The ID of the parameter set
    :param is_active: If the parameter set should be set to active or inactive
    :return: None
    """
    url = get_url(base_url) + "/" + str(param_set_id)
    update = {"is_active": is_active}
    try:
        response = requests.patch(url, json=update, timeout=5)
        if handle_modify(response, "Parameter Set", param_set_id):
            print("Parameter Set", param_set_id, "active status changed to", is_active)
    except ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)


def list_param_sets(base_url):
    """
    List all the parameter sets in the Ringling Service
    :param base_url: The URL of the Ringling Service
    :return: None
    """
    perform_list(get_url(base_url))