'''Methods related to handling project settings.'''

import logging
import yaml

logging.basicConfig(filename='basilpi.log', level=logging.DEBUG)


def load_settings(filename='settings.yaml'):
    """Read settings from a file.

    Keyword arguments:
    filename -- the source file (default settings.yaml)
    """
    with open(filename, 'r') as settings_yaml:
        logging.debug("Reading settings from file: %s", filename)
        return yaml.load(settings_yaml)


def save_settings(settings_dict, filename='settings.yaml'):
    """Write settings to a file.

    Keyword arguments:
    settings_dict -- the settings dictionary to write out
    filename -- the destination file (default settings.yaml)
    """
    with open(filename, 'w') as file_handle:
        yaml.dump(settings_dict, file_handle, default_flow_style=False)
        logging.debug("Saved settings to file: %s", filename)
