import pickle 
import os 
import sys 

from src.exception import CustomException
from src.logger import logging


def save_object(object, save_path: str):
    '''
    saves the object at given path (including filename) using pickle in 'ab' format
    Params:
        object: any - the object which needs to be dumped or saved
        save_path: str - location (including filename) where to save the object
    Returns:
        None
    '''
    try:
        dir_path = os.path.dirname(save_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(save_path, 'ab') as save_file:
            pickle.dump(object, save_file)
        
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
    
    
def load_object(load_path: str):
    '''
    loads the object at given path (including filename) using pickle in 'rb' format
    Params:
        load_path: str - location (including filename) from where to load the object
    Returns:
        object: any
    '''
    try:
        with open(load_path, 'rb') as load_file:
            return pickle.load(load_file)
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
    
    
def reformat_prediction(prediction: dict) -> dict:
    '''
    Reformat the prediction dictionary by removing the unwanted values, and type conversion
    Params:
        prediction: dict - the prediction dict generated by the prediction pipeline
    Returns: 
        the reformatted predictions: dict
    '''
    try:
        formatted_prediction = dict()
        formatted_prediction['query'] = prediction['query']
        formatted_prediction['answers'] = []
        
        for answer_obj in prediction['answers']:
            answer_obj = answer_obj.to_dict()
            
            formatted_prediction['answers'].append(
                {
                    'answer': answer_obj['answer'],
                    'context': answer_obj['context']
                }
            )
        
        return formatted_prediction
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
    
    
def check_model_exist(save_path: str) -> bool:
    '''
    check if the model save file exist or it needs to be trained
    Params:
        save_path: str - path where the model supposed to be saved
    Returns:
        True if model is saved else False: bool
    '''
    
    try:
        if os.path.isfile(save_path):
            return True 
        else:
            return False 
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
    