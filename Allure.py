import allure
from allure_commons.types import AttachmentType


def screenshot(driver, screenshot_title):
    with allure.step({screenshot_title}):
        allure.attach(driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
