import yaml
from importlib import import_module

def execute_functions(name = 'test'):
    functions = None
    with open('execution\commands.yml', 'r') as f:
        data = yaml.full_load(f)
    for command in data.get('commands'):
        if command.get('name') == name:
            functions = command["functions"]
            if command.get('message'):
                print(command.get('message'))
            break
    if functions == None:
        raise Exception('No function found')
    for kwargs in functions:
        if kwargs.get('message'):
            print(kwargs.get('message'))
        function = kwargs["function"]
        mod_get = kwargs.get("module")
        module = import_module(mod_get or 'extraction.functions')
        obj = getattr(module, function)
        obj(**kwargs)

def list_commands():
    with open('execution\commands.yml', 'r') as f:
        data = yaml.full_load(f)
    for command in data.get('commands'):
        name = command.get('name')
        desc = command.get('description')
        print(f"{name}: {desc}")