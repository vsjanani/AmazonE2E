from selenium.webdriver.common.by import By


class Locator:
    start_Here = (By.PARTIAL_LINK_TEXT, "Start here")
    your_Name = (By.CSS_SELECTOR, "input[name='customerName']")
    mobile_Number = (By.ID, "ap_phone_number")
    email_Optional = (By.CSS_SELECTOR, "[type='email']")
    pass_Word = (By.ID, "ap_password")
    continue_Login = (By.CSS_SELECTOR, "#auth-continue")
    failure_Message = (By.CSS_SELECTOR, "[class='a-list-item']")