from selenium.webdriver.common.by import By

from pageObjects.practicecreateaccountpage import CreateAccountPage
# from utilities.usefixture import UseFixture


class PracticeAmazonDropDown:
    def __init__(self, webdriverObj):
        self.webdriverObj = webdriverObj
        self.dropdown = self.webdriverObj.find_element(By.CSS_SELECTOR, 'select[name="url"]')
        self.accountLists = self.webdriverObj.find_element(By.ID, "nav-link-accountList")

    def drop_down(self):
        return self.dropdown

    def account_lists(self):
        return self.accountLists










