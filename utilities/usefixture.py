import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("test_dawn_dusk")
class UseFixture:

    def select_option(self, locator, text):
        categories = Select(locator)
        categories.select_by_visible_text(text)

    def logging(self):
        logObj = logging.getLogger(inspect.stack()[1][3])
        fileHandler = logging.FileHandler("Logfile.log")
        formatter = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
        logObj.addHandler(fileHandler)
        fileHandler.setFormatter(formatter)
        logObj.setLevel(logging.DEBUG)
        return logObj

    def expWait(self, locator):
        return WebDriverWait(self.webdriverObj, 10).until(expected_conditions.presence_of_element_located(locator))\
            .get_attribute("value")

    # def getAttribute(self, locator):
    #      self.getAttribute = locator.get_attribute("value")
    #      return self.getAttribute


# def mouse_hover(self, locator):
#     mouseHover = ActionChains(self.webdriverObj)
#     mouseHover.move_to_element(locator)






