import os
import importlib
import inspect

folder_name = "handler"

def handler():
    fncs = []
    commands = {}
    files = os.listdir(folder_name)
    for file in files:
        module = importlib.import_module(f"{folder_name}.{file.split(".")[0]}")
        # fncs.append(getattr(module, ""))
        fncs.append(inspect.getmembers(module, inspect.isfunction))
    for fnc in fncs[:-1]:
        commands.update(fnc)
    return commands