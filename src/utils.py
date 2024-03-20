import os
import sys

import numpy as np
import pandas as pd
import dill# import the dill library to save the object in pkl format

from src.exception import CustomException


def save_object(file_path,obj):
    '''
    Function to save the object
    '''
    try:
        dir_path=os.path.dirname(file_path)#get the directory path

        os.makedirs(dir_path,exist_ok=True)#create the directory if it does not exist

        with open(file_path,"wb") as file:#open the file in write mode
            dill.dump(obj,file)#dump the object into the file

    except Exception as e:
        raise CustomException(e,sys)