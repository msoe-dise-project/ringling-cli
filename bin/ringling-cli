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

import argparse
from ringling.test_script import print_test
from ringling.projects import create_project
from ringling.projects import list_projects
from ringling.projects import get_project

def parseargs():
    parser = argparse.ArgumentParser()

    object_type_choices = ["project", "param-set", "deploy-status", "model-test-results"]
    action_choices = ["get", "create", "list"]

    parser.add_argument("base_url",
                        type = str)

    parser.add_argument("object_type",
                        type = str,
                        choices = object_type_choices)

    parser.add_argument("action",
                        type = str,
                        choices = action_choices)

    parser.add_argument("-N", "--name",
                    type = str,
                    required = False)

    parser.add_argument("--id",
                type = int,
                required = False)

    #Create a URL argument

    return parser.parse_args()

if __name__ == "__main__":
    args = parseargs()

    base_url = args.base_url
    if base_url == "localhost":
        base_url = "http://localhost:8888"

    if args.object_type == "project":
        if args.action == "get":
            if args.id == None:
                print("This action required an integer id to be specified using --id")
            else:
                get_project(base_url, args.id)
        elif args.action == "create":
            if args.name == None:
                print("This action requires a name to be specified using --name or -N")
            else:
                create_project(base_url, args.name)
        elif args.action == "list":
            list_projects(base_url)
