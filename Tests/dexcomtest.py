import allure
import pytest
from selpy.driver import Driver
from Pages.dexcom_home_page import DexcomHomePage
from selpy.variable import Var


# Feature name and severity to have better reporting in the allure.
@allure.feature("Creating a simple test in dexcom")
@allure.severity('Critical')
@pytest.mark.regression  # Custom pytest marker to run the test cases with ease on demand
@pytest.mark.ui  # Custom pytest marker to run the test cases with ease on demand
def test_login_001():
    with allure.step("Initialize the UI dynamic data"):
        ui_dynamic_data = {}
    with allure.step("Set the test data file needed for this test run"):
        static_variable = Var("dexcom.yml", "static")  # static variables will change for each test case/ test module

    with allure.step("Initialize the driver and navigate to the url and Click on Home Users"):
        driver = Driver()  # Initialize the driver. Driver configurations will be taken from the global_data.yml file
        driver.get(static_variable.static_value_for("url"))
        assert (DexcomHomePage.click_homepage() is True), "Clicked on Home Users"

    with allure.step("Fetch Username from file and enter"):
        DexcomHomePage.input_username(static_variable.static_value_for("username"))

    with allure.step("Fetch password from file and enter"):
        DexcomHomePage.input_password(static_variable.static_value_for("password"))

    with allure.step("Click on login page"):
        DexcomHomePage.click_homepage()


