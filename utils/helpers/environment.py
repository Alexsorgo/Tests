import os
from dotenv import load_dotenv

from project_constants import project_path
from utils.logs import log

load_dotenv(dotenv_path=os.path.join(project_path, ".env"), verbose=True)


def get_environment(env_variable):
    value = os.getenv(env_variable)
    if value is None:
        return log.debug("------- ATTENTION!!! {}: has not been set. -------".format(env_variable))
    log.debug("{0}: {1}".format(env_variable, value))
    return value
