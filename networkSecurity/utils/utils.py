import os
import sys
import yaml
from networkSecurity.components.exception import customException
import numpy as np
import pickle

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
    
def save_numpy_arr(file_path:str, array:np.array):
    try:
        dir_path=os.path.dirname(file_path)    
        os.makedirs(dir_path, exist_ok=True)
        with open (file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise customException(e, sys)

def save_obj(file_path:str, obj:object)->None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise customException(e,sys)
                            