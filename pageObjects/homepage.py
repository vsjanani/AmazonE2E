from selenium.webdriver.common.by import By

from pageObjects.searchresults import SearchResults


class HomePage:
    def __init__(self, webdriverObj):
        self.webdriverObj = webdriverObj
        self.searchBar = self.webdriverObj.find_element(By.CSS_SELECTOR, "#search_query_top")
        self.searchButton = self.webdriverObj.find_element(By.CSS_SELECTOR, "button[name = 'submit_search']")

    def search_bar(self):
        return self.searchBar

    def search_button(self):
        self.searchButton.click()
        searchResultsPageObj = SearchResults(self.webdriverObj)
        return searchResultsPageObj



