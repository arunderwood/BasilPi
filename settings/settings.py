import yaml
import logging

logging.basicConfig(filename='basilpi.log',level=logging.DEBUG)

def load_settings(file='settings.yaml'):
    with open(file, 'r') as settings_yaml:
        logging.debug("Reading settings from file: %s" % file)
        return yaml.load(settings_yaml)

def save_settings(settings_dict, file='settings.yaml'):
    with open(file, 'w') as f:
        yaml.dump(settings_dict, f, default_flow_style=False)
        logging.debug("Saved settings to file: %s" % file)
