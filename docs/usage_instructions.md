# ringling-cli
Command-line interface for the Ringling model management service

## Using ringling-cli
The CLI is used by running commands in the following format:

ringling-cli [host] [object-type] [action] [params]

Where:  
[host] is the url of the management process. Generally, it is ok to leave this as "localhost".

[object-type] is the type of object you wish to interface with, and is one of: ["project", "param-set", "deploy-status", "model-test-results"]

[action] is the action you wish to perform. This may vary from object type to object type (see below), but is generally one of: ["get", "create", "modify", "list"]

[params] represents command specific parameters. See below for more detail.  
--id to specify id  
--name or -N to specify the name  
--active or -A to specify set activity

## Interfacing with projects
The following commands can be used to create, list, and get projects.


#### Create
Input:  

```
ringling-cli localhost project create -N name_here
```

Output:

```
Project name_here created successfully  
Project ID: 4
```

#### List
Input:

```
ringling-cli localhost project list
```

Output:

```  
{'projects': [{'project_id': 1, 'project_name': 'test'},  
              {'project_id': 2, 'project_name': 'test2'}]}  
```

#### Get
Input:  

```
ringling-cli localhost project get --id 1
```

Output:  

```
{'project_id': 1, 'project_name': 'test'}
```

## Interfacing with Parameter Sets
The following commands can be used to create, list, modify, and get paramater sets.

#### Create
###### Alternative 1:  
Input:  
```
ringling-cli localhost param-set create --id 1 --params "{\"Param1\":\"Val1\"}" --active False
```

Output:
```
Parameter Set created successfully with ID 1
```

###### Alternative 2 (Single quotes internally converted to double quotes for json parsing due to windows command line limitations):  
Input:  
```
ringling-cli localhost param-set create --id 1 --params "{'Param1':'Val1'}" --active False
```

Output:
```
Parameter Set created successfully with ID 2
```

###### Alternative 3:  
Input:  
```
ringling-cli localhost param-set create --id 2 --params "C:\Users\path\to\file.json" --active False
```

Output:
```
Parameter Set created successfully with ID 3
```

#### List
Input:  
```
ringling-cli localhost param-set list
```

Output:

```  
{'parameter_sets': [{'is_active': True,
                     'parameter_set_id': 1,
                     'project_id': 5,
                     'training_parameters': {'param1': 1, 'param2': '2'}},
                    {'is_active': False,
                     'parameter_set_id': 2,
                     'project_id': 5,
                     'training_parameters': {'param1': 1, 'param2': '3'}}]}
```

#### Get
Input:  

```
ringling-cli localhost param-set get --id 1
```

Output:  

```
{'is_active': True,
 'parameter_set_id': 1,
 'project_id': 5,
 'training_parameters': {'param1': 1, 'param2': '2'}}
```

#### Modify
Input:  

```
ringling-cli localhost param-set get --id 1
```

Output:  

```
{'is_active': True,
 'parameter_set_id': 1,
 'project_id': 5,
 'training_parameters': {'param1': 1, 'param2': '2'}}
```
