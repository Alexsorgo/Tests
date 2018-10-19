import os

from tests.configs import config

project_path = os.path.abspath(os.path.dirname(__file__))
version = "{}: {} - {}".format(config.DEVICE_NAME, config.PLATFORM_NAME, config.PLATFORM_VERSION)
