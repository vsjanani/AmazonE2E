from selenium.webdriver.common.by import By
# from tests.practiceerrormessagepage import ErrorMessagePage
from pageObjects.locators import Locator
from tests.practiceerrormessagepage import ErrorMessagePage


class CreateAccountPage:
    def __init__(self, webdriverObj):
        self.webdriverObj = webdriverObj
        # locator = Locator()
        self.yourName = self.webdriverObj.find_element(*Locator.your_Name)
        self.mobileNumber = self.webdriverObj.find_element(*Locator.mobile_Number)
        self.emailOptional = self.webdriverObj.find_element(*Locator.email_Optional)
        self.passWord = self.webdriverObj.find_element(*Locator.pass_Word)
        self.continueLogin = self.webdriverObj.find_element(*Locator.continue_Login)

    # def get_yourName_field(self):
    #     return self.yourName

    def get_continue_field(self):
        self.continueLogin.click()
        errorMessageObj = ErrorMessagePage(self.webdriverObj)
        return errorMessageObj




