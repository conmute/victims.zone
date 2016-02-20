import os

def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))
    
def get_config_folder_path():
    return os.path.join(os.path.abspath(os.path.join(get_app_base_path(), os.pardir)), 'config')