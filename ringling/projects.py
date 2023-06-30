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

import json
import requests

def get_url():
    """
    Get the URL for interacting with projects
    :return: The project URL
    """
    return "http://localhost:8888/v1/projects"


def create_project(project_name):
    """
    Create a project on the Ringling service
    :param project_name: The name of the project to create
    :return: The response from the service
    """
    obj = {"project_name": project_name}
    try:
        response = requests.post(get_url(),
                                 json=obj)
        if response.status_code == 201:
            response_json = response.json()
            print(f"Project {project_name} created successfully")

            print("Project ID:", response_json['project_id'])
    except requests.exceptions.ConnectionError:
        print("Failed to connect to model management service. Make sure Ringling is running.")

def list_projects():
    """
    List all the projects in the Ringling Service
    :return: None
    """
    try:
        response = requests.get(get_url())
        response_json = response.json()
        print(json.dumps(response_json, indent=1))
    except requests.exceptions.ConnectionError:
        print("Failed to connect to model management service. Make sure Ringling is running.")

def get_project(project_id):
    """
    Return information about a specific project in the Ringling Service by ID
    :param project_id:
    :return:
    """
    url = get_url() + "/" + str(project_id)
    try:
        response = requests.get(url)
        if response.status_code == 500:
            print("Invalid Project ID")
        else:
            response_json = response.json()
            print(json.dumps(response_json, indent=1))
    except requests.exceptions.ConnectionError:
        print("Failed to connect to model management service. Make sure Ringling is running.")
