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
import argparse
import sys
import os
from ringling.test_script import print_test
from ringling.projects import create_project
from ringling.projects import list_projects
from ringling.projects import get_project
from ringling.param_sets import create_param_set
from ringling.param_sets import list_param_sets
from ringling.param_sets import get_param_set
from ringling.param_sets import modify_param_set


def parse_boolean(arg):
    if arg in ("True", "true", 1):
        return True
    elif arg in ("False", "false", 0):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url", type=str,)
    subparsers = parser.add_subparsers(dest="object", required=True)

    project_parser = subparsers.add_parser("project", help="Project interaction")
    project_parsers = project_parser.add_subparsers(dest="action")

    project_get_parser = project_parsers.add_parser("get", help="Get project by ID")

    project_get_parser.add_argument("--id",
                                    type=int,
                                    required=True,
                                    help="An project ID specifying the project to return")

    project_create_parser = project_parsers.add_parser("create", help="Create project given a name")

    project_create_parser.add_argument("-N", "--name",
                                       type=str,
                                       required=True,
                                       help="The name for the newly created project")

    project_parsers.add_parser("list", help="List projects")

    param_parser = subparsers.add_parser("param-set", help="Project interaction")
    param_parsers = param_parser.add_subparsers(dest="action")

    param_get_parser = param_parsers.add_parser("get", help="Get parameter set by ID")

    param_get_parser.add_argument("--id",
                                  type=int,
                                  required=True,
                                  help="An integer ID specifying the parameter set to return")

    param_create_parser = param_parsers.add_parser("create", help="Create a parameter set")

    param_create_parser.add_argument("--id",
                                     type=int,
                                     required=True,
                                     help="An integer ID specifying the project that the parameter set is linked to")

    param_create_parser.add_argument("-P", "--param-file",
                                     type=str,
                                     required=True,
                                     dest="params",
                                     help="A path to a json formatted file with the parameter values")

    param_create_parser.add_argument("-S", "--set-status",
                                     type=parse_boolean,
                                     required=True,
                                     dest="active",
                                     help="A boolean specifying if the set is active")

    param_modify_parser = param_parsers.add_parser("modify", help="Modify the activity status of a parameter set")

    param_modify_parser.add_argument("--id",
                                     type=int,
                                     required=True,
                                     help="An integer ID specifying the parameter set to modify")

    param_modify_parser.add_argument("-S", "--set-status",
                                     type=parse_boolean,
                                     required=True,
                                     dest="active",
                                     help="A boolean specifying if the set is active")

    param_parsers.add_parser("list", help="List parameter sets")

    return parser.parse_args()


if __name__ == "__main__":
    args = parseargs()

    base_url = args.base_url
    if base_url == "localhost":
        base_url = "http://localhost:8888"

    if args.object == "project":
        if args.action == "get":
            get_project(base_url, args.id)
        elif args.action == "create":
            create_project(base_url, args.name)
        elif args.action == "list":
            list_projects(base_url)

    elif args.object == "param-set":
        if args.action == "get":
            get_param_set(base_url, args.id)
        elif args.action == "create":
            try:
                if args.params.endswith(".json"):
                    if not os.path.isfile(args.params):
                        print("Specified file does not exist", file=sys.stderr)
                        sys.exit(1)
                    with open(args.params, 'r', encoding='utf-8') as file:
                        params = json.load(file)
                        create_param_set(base_url, args.id, params, args.active)
                else:
                    print("Specified file must be json", file=sys.stderr)
                    sys.exit(1)
            except json.decoder.JSONDecodeError:
                print("Specified params must be a path to a valid JSON file", file=sys.stderr)
                sys.exit(1)
        elif args.action == "modify":
            modify_param_set(base_url, args.id, args.active)
        elif args.action == "list":
            list_param_sets(base_url)