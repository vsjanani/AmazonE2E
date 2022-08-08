from selenium.webdriver.common.by import By


class SearchResults:
    def __init__(self, webdriverObj):
        self.webdriverObj = webdriverObj
        self.selectProduct = self.webdriverObj.find_element(By.XPATH, '//div[@id = "center_column"]/ul/li[1]')
        self.addToCart = self.webdriverObj.find_element(By.XPATH, '//a[@title = "Add to cart"]')
        # self.hoverToItem = self.webdriverObj.find_element((By.XPATH, '//div[@id = "center_column"]/ul/li[1]'))

    def select_product(self):
        return self.selectProduct

    def add_to_cart(self):
        return self.addToCart

    # def hover_to_item(self):
    #     return self.hoverToItem
    #

