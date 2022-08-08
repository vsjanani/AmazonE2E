from pageObjects.locators import Locator


class StartHere:
    def __init__(self, webdriverObj):
        self.webdriverObj = webdriverObj
        self.startHere = self.webdriverObj.find_element(*Locator.start_Here)

    def start_here(self):
        return self.startHere

