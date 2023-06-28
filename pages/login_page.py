import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = 'https://ohota26.ru/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    login_button = "//input[@type='email']"
    password = "//input[@type='password']"
    enter_button = "//button[@class='btn btn-dark btn-submit w100 mb20']"


    """Getters"""

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))


    """Actions"""

    def input_login_button(self, user_name):
        self.get_login_button().send_keys(user_name)
        print("Input Login Button")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("CLick Enter Button")


    """Methods"""

    """Вводим данные для авторизации на сайте и входим на сайт"""
    def authorisation(self):
        self.driver.get(self.url) # Метод, который открывает нашу url
        self.driver.maximize_window()
        self.get_current_url()
        self.input_login_button("test.qa@yandex.ru")
        self.input_password("11223344")
        self.click_enter_button()




