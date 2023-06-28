import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class User_data_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    main_page_button = "//a[@class='header__logo flb-csb']"


    """Getters"""

    def get_main_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_page_button)))


    """Actions"""

    def click_main_page_button(self):
        self.get_main_page_button().click()
        print("CLick Main Page Button")


    """Methods"""

    """Переходим на главную страницу со страницы личного кабинета пользователя"""
    def select_main_page(self):
        Logger.add_start_step(method='select_main_page')
        self.click_main_page_button()
        self.assert_url("https://ohota26.ru/")
        Logger.add_end_step(url=self.driver.current_url, method='select_main_page')



