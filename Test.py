import os

import pytest
from appium import webdriver as AppiumDriver

import Autorization
import Qase


code = os.environ['CODE']
plan_id = os.environ['PLAN_ID']


@pytest.mark.parametrize('udid', Autorization.udid.values(), ids=Autorization.udid)
@pytest.mark.parametrize('case', Qase.get_plan(code, plan_id))
def test_init(case, udid):
    capabilities = {
        "appium:platformName": "Android",
        "appium:udid": udid
    }
    driver = AppiumDriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    case = Qase.get_case(code, case)
    Qase.launch_step(case['steps'], driver)



