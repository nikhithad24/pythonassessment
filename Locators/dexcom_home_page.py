from selpy.locator import Locator
# Importing the locator method from selpy


class DexComHomePageLocator:
    # Use the following description for different locators
    # CSS - 'css selector'
    # XPATH - 'xpath'
    # ID - 'id'
    # NAME - 'name'
    # LINK TEXT - 'link text'
    # PARTIAL LINK TEXT - 'partial link text'
    # TAG NAME - 'tag name'
    # CLASS NAME - 'class name'
    dexcom_home_users = Locator("xpath", "//a[text()='Dexcom CLARITY for Home Users']")
    # In chrome amazon_search_categories works fine for select
    # In firefox we have an open issue with the
    dexcom_username = Locator("xpath", "//input[@id='username']")
    dexcom_password = Locator("xpath", "//*[@id='password']")
    dexcom_button = Locator("xpath", "//*[@id='edit-actions']/input")

    def __init__(self):
        print("Locators for Dexcom home page")


