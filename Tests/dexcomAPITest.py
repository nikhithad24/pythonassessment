import requests
import allure
import pytest
from selpy.driver import Driver
from Pages.dexcom_home_page import DexcomHomePage
from selpy.variable import Var


def login_api_test():
    static_variable = Var("dexcom.yml", "static")
    response=requests.get(static_variable.static_value_for("url"))
    print(response.status_code)
    postresponse = requests.post(static_variable.static_value_for("api"))
    print(postresponse.headers)