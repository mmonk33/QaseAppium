import os
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess

import Allure
import Locators


class Remote:
    def __init__(self, driver):
        self.driver = driver

    def down(self):
        self.driver.press_keycode(20)

    def up(self):
        self.driver.press_keycode(19)

    def left(self):
        self.driver.press_keycode(21)

    def right(self):
        self.driver.press_keycode(22)

    def ok(self):
        self.driver.press_keycode(23)

    def home(self):
        self.driver.press_keycode(3)

    def back(self):
        self.driver.press_keycode(4)

    def settings(self):
        self.driver.press_keycode(82)

    def reset(self):
        self.driver.resetApp()


def find_element(driver, locator, timer=10):
    return WebDriverWait(driver, timer).until(EC.presence_of_element_located(locator),
                                              message=f"Can't find element by locator {locator}")


class ADB:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def package_installed(package):
        return str(subprocess.check_output(f'docker exec -i container-appium adb shell \"su -c \'pm list packages | '
                                           f'grep {package} \'\"', shell=True))

    @staticmethod
    def app_version(package_name):
        return str(float(subprocess.check_output(
            f'docker exec -it container-appium adb shell dumpsys package {package_name} | grep versionName',
            shell=True)))

    @staticmethod
    def reboot_devcie():
        os.system(f'docker exec -i container-appium adb shell reboot')

    @staticmethod
    def current_app():
        return str((subprocess.check_output(
            f"docker exec -i container-appium adb shell dumpsys activity recents | grep 'Recent #0' | cut -d= -f2 | "
            f"sed 's| .*||' | cut -d '/' -f1",
            shell=True)))

    def device_version(self):
        return str(self.driver.desired_capabilities['platformVersion'])


def check_package(driver, expected):
    actual = ADB.current_app()
    assert expected in actual, f'Not expected'


def check_element_text(driver, locator, expected):
    locator = locator.replace("\\", '')
    locator = eval(f'Locators.{locator}')
    actual = find_element(driver, locator).text
    assert actual in expected, f"NOT EQUAL ELEMENT"


def click(driver, locator):
    locator = locator.replace("\\", '')
    locator = eval(f'Locators.{locator}')
    find_element(driver, locator).click()


def wait(driver, sec):
    time.sleep(int(sec))


def start_activity(driver, package):
    activity = package.split()
    driver.start_activity(activity[0], activity[1])


functions = {
    'Press down': Remote.down,
    'Press up': Remote.up,
    'Press left': Remote.left,
    'Press right': Remote.right,
    'Press ok': Remote.ok,
    'Press home': Remote.home,
    'Press back': Remote.back,
    'Press settings': Remote.settings,
    'Package installed': ADB.package_installed,
    'Click': click,
    'Start': start_activity,
    'Screenshot': Allure.screenshot,
    'Check package': check_package,
    'Check element text': check_element_text,
    'Wait': wait
}

