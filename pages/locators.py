from selenium.webdriver.common.by import By


class MainPageLocators():
    login_url = ("selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')

