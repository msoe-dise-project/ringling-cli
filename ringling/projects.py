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
from ringling.response_handling import handle_create
from ringling.response_handling import handle_get


def get_url(base_url):
    """
    Get the URL for interacting with projects
    :return: The project URL
    """
    return base_url + "/v1/projects"


def create_project(base_url, project_name):
    """
    Create a project on the Ringling service
    :param base_url: The URL of the Ringling Service
    :param project_name: The name of the project to create
    :return: The response from the service
    """
    obj = {"project_name": project_name}
    try:
        response = requests.post(get_url(base_url),
                                 json=obj, timeout=5)
        if handle_create(response):
            response_json = response.json()
            print(f"Project {project_name} created successfully")
            print("Project ID:", response_json['project_id'])
        else:
            sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)

def list_projects(base_url):
    """
    List all the projects in the Ringling Service
    :param base_url: The URL of the Ringling Service
    :return: None
    """
    try:
        response = requests.get(get_url(base_url), timeout=5)
        response_json = response.json()
        pprint.pprint(response_json)
    except requests.exceptions.ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)

def get_project(base_url, project_id):
    """
    Return information about a specific project in the Ringling Service by ID
    :param base_url: The URL of the Ringling Service
    :param project_id:
    :return: None
    """
    url = get_url(base_url) + "/" + str(project_id)
    try:
        response = requests.get(url, timeout=5)
        if handle_get(response, "Project", project_id):
            response_json = response.json()
            pprint.pprint(response_json)
        else:
            sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Can not connect to model management service. Is Ringling running?", file=sys.stderr)
        sys.exit(1)
