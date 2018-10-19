import pytest

from tests.configs import config
from tests.utils.desired_capabilities import DC
from tests.utils.driver_setup.driver_setup import Drivers

from tests.utils.logs import log


@pytest.fixture()
def remove_app():
    cmd = 'adb uninstall com.nynja.mobile.communicator'
    import subprocess
    subprocess.Popen(cmd.split())


@pytest.fixture()
def base_driver_setup(request):
    test_name = 'some'
    version = "{}: {} - {}".format(config.DEVICE_NAME, config.PLATFORM_NAME, config.PLATFORM_VERSION)

    log.debug("Start test: '{}'.".format(test_name))

    driver = Drivers.create_mobile("http://0.0.0.0:4723/wd/hub", {})
    request.cls.driver = driver

    yield

    # TODO: Implement process listener
    # if request.node.rep_setup.failed or request.node.rep_call.failed:
    #     try:
    #         driver.save_screenshot_as_file(project_constants.version + "_" + test_name)
    #     except Exception as e:
    #         log.error("Could not create screenshot or save html source. Error: {}. "
    #                   "\n May be driver was not initialized".format(e))
    try:
        driver.save_screenshot_as_file(version + "_" + test_name)
    except Exception as e:
        log.error("Could not create screenshot or save html source. Error: {}. "
                  "\n May be driver was not initialized".format(e))
    driver.quit()
