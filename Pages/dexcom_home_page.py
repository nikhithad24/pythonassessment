from Locators.dexcom_home_page import DexComHomePageLocator


# Inherit the locator class inside page class for easier access of locators
class DexcomHomePage(DexComHomePageLocator):

    def __init__(self):
        super().__init__()

    @classmethod
    def input_username(cls, string):
        DexComHomePageLocator.dexcom_username.send_keys(string)

    @classmethod
    def input_password(cls, string):
        DexComHomePageLocator.dexcom_username.send_keys(string)

    @classmethod
    def click_login(cls):
        return DexComHomePageLocator.dexcom_button.click()

    @classmethod
    def click_homepage(cls):
        return DexComHomePageLocator.dexcom_home_users.click()
