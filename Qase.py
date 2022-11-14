import pytest
import requests
import Funcs
from termcolor import cprint
import Autorization


class Init:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Token": Autorization.token
    }


def get_plan(code, plan_id):
    url = f"https://api.qase.io/v1/plan/{code}/{plan_id}"
    response = requests.get(url, headers=Init.headers).json()
    cases = []
    for case in response['result']['cases']:
        cases.append(case['case_id'])
    return cases


def create_test_run(plan_id, test_run_title):
    url = "https://api.qase.io/v1/run/W370"
    payload = {
        "title": {test_run_title},
        "plan_id": {plan_id}
    }
    response = requests.post(url, json=payload, headers=Init.headers)
    return response.json()


def launch_step(case, driver):
    for step in case:
        if step['data'] is None:
            launch_step_without_data(driver, step['action'])
        else:
            if step['expected_result'] is not None:
                launch_step_without_data_expected_result(driver, step['action'], step['data'], step['expected_result'])
            else:
                launch_step_with_data(driver, step['action'], step['data'])


def launch_step_without_data_expected_result(driver, step_title, input_data, expected_result):
    try:
        step_action = Funcs.functions[step_title](driver, input_data, expected_result)
        return step_action
    except KeyError:
        pytest.skip(cprint(f"\nFunction \"{step_title}\" not defined in Funcs.py", 'red'))


def launch_step_without_data(driver, step_title):
    try:
        remote = Funcs.Remote(driver)
        step_action = Funcs.functions[step_title](remote)
        return step_action
    except KeyError:
        pytest.skip(cprint(f"\nFunction \"{step_title}\" not defined in Funcs.py", 'red'))


def launch_step_with_data(driver, step_title, input_data):
    try:
        step_action = Funcs.functions[step_title](driver, input_data)
        return step_action
    except KeyError:
        pytest.skip(cprint(f"\nFunction \"{step_title}\" not defined in Funcs.py", 'red'))


def get_case(code, cases):
    url = f"https://api.qase.io/v1/case/{code}/{cases}"
    response = requests.get(url, headers=Init.headers).json()
    return response['result']


def expected_result(responce):
    for step in responce['result']['steps']:
        return step['expected_result']


def input_data(responce):
    for step in responce['result']['steps']:
        return step['data']


def create_defect(code, title, actual_result, severity):
    url = f"https://api.qase.io/v1/defect/{code}"

    payload = {
        "title": title,
        "actual_result": actual_result,
        "severity": severity
    }
    response = requests.post(url, json=payload, headers=Init.headers)
    return response


def case_name(response):
    return response['result']['title']
