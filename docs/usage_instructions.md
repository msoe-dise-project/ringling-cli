# ringling-cli
Command-line interface for the Ringling model management service

## Using ringling-cli
The CLI is used by running commands in the following format:

ringling-cli [host] [object-type] [action] [params]

Where:  
[host] is the url of the management process. Generally, it is ok to leave this as "localhost".

[object-type] is the type of object you wish to interface with, and is one of: ["project", "param-set", "deploy-status", "model-test-results"]

[action] is the action you wish to perform. This may vary from object type to object type (see below), but is generally one of: ["get", "create", "modify", "list"]

[params]

## Interfacing with projects
The following commands can be used to create, list, and get projects.


#### Create
Input:  
ringling-cli localhost project create -N name_here

Output:  
Project name_here created successfully  
Project ID: 4

#### List
Input:  
ringling-cli localhost project list

Output:  
{'projects': [{'project_id': 1, 'project_name': 'test'},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{'project_id': 2, 'project_name': 'test'}]}  

#### Get
Input:  
ringling-cli localhost project get --id 1

Output:  
{'project_id': 1, 'project_name': 'test'}
