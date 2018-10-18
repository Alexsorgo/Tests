from configs import config
from utils.logs import log


class DC:

    @staticmethod
    def set_capabilities():
        """
        This is to set desired capabilities for Appium. All parameters are set in UI/configs/config.ini file
        :return:
        """
        log.info("Set desired capabilities for %s", config.PLATFORM_NAME)

        caps = {"deviceName": config.DEVICE_NAME + " Device",
                "platformName": config.PLATFORM_NAME,
                "platformVersion": config.PLATFORM_VERSION,
                'bundleId': config.BUNDLE_ID,
                # "appPackage": "com.nynja.mobile.communicator",
                # "appActivity": "com.nynja.mobile.communicator.ui.activities.SplashActivity",
                # "noReset": "true"
                # TODO: Issue with send keys action (Appium)
                # "automationName": "UiAutomator2"
                }

        if config.UDID:
            caps.update({"udid": config.UDID})

        # TODO: This for future implementation cross platform feature
        # if caps["platformName"] == "iOS":
        #     caps.update({"xcodeOrgId": config.xcode_org_id, "xcodeSigningId": config.xcode_signing_id,
        #                  "automationName": "XCUITest"})
        return caps
