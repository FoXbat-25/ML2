import os
import sys
import yaml
from networkSecurity.components.exception import customException
def read_yaml_file(file_path)->dict:
    try:
        with open(file_path, 'rb') as file_obj:
            return yaml.safe_load(file_obj)
    except Exception as e:
        raise customException(e, sys)

def write_yaml_file(file_path:str, content:object, replace:bool = True):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                yaml.dump(content, file)
    except Exception as e:
        raise customException(e,sys)                