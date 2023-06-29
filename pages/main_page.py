import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    catalog_button = "//button[@class='header__btn-catalog btn btn-dark flb-csb']"
    type_product_button_1 = "/html/body/div[2]/div/nav[1]/div[5]/a/span"
    type_product_button_2 = "/html/body/main/div[2]/div/div/div[1]/a[7]"
    search = "//input[@name='search']"
    whats_app_button = "/html/body/div[1]/div/div/div[2]/div[2]/a[1]"
    telegram_button = "/html/body/div[1]/div/div/div[2]/div[2]/a[2]"
    vk_button = "/html/body/div[1]/div/div/div[2]/div[2]/a[3]"

    """Getters"""

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_type_product_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_product_button_1)))

    def get_type_product_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_product_button_2)))

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_whats_app_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.whats_app_button)))

    def get_telegram_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram_button)))

    def get_vk_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vk_button)))

    """Actions"""

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Catalog Button")

    def click_type_product_button_1(self):
        self.get_type_product_button_1().click()
        print("Click Type Product Button_1")

    def click_type_product_button_2(self):
        self.get_type_product_button_2().click()
        print("Click Type Product Button_2")

    def input_search(self, search):
        self.get_search().send_keys(search)
        print("Input Search")

    def click_whats_app_button(self):
        self.get_whats_app_button().click()
        print("Click WhatsApp Button")

    def click_telegram_button(self):
        self.get_telegram_button().click()
        print("Click Telegram Button")

    def click_vk_button(self):
        self.get_vk_button().click()
        print("Click VK Button")

    """Methods"""

    """Выбор определенных продуктов из меню"""
    def select_menu(self):
        with allure.step("Select menu"):
            Logger.add_start_step(method='select_menu')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.click_catalog_button()
            self.click_type_product_button_1()
            self.click_type_product_button_2()
            Logger.add_end_step(url=self.driver.current_url, method='select_menu')

    """Используем строку поиска по слову Ласты"""
    def search_1(self):
        with allure.step("Search 1"):
            Logger.add_start_step(method='search_1')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.input_search("Ласты\n")
            # self.driver.send_keys(Keys.RETURN)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search_1')

    """Используем строку поиска по слову Блесна"""
    def search_2(self):
        with allure.step("Search 21"):
            Logger.add_start_step(method='search_2')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.input_search("Блесна\n")
            # self.driver.send_keys(Keys.RETURN)c
            Logger.add_end_step(url=self.driver.current_url, method='search_2')


    """Используем строку поиска по слову Лодка"""
    def search_3(self):
        with allure.step("Search 3"):
            Logger.add_start_step(method='search_3')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.input_search("Лодка\n")
            # self.driver.send_keys(Keys.RETURN)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search_3')

    """Переход в мессенджер WhatsApp"""
    def messenger_whats_app(self):
        with allure.step("Messenger WhatsApp"):
            Logger.add_start_step(method='messenger_whats_app')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.click_whats_app_button()
            time.sleep(2)
            self.assert_url("https://ohota26.ru/")
            Logger.add_end_step(url=self.driver.current_url, method='messenger_whats_app')

    """Переход в мессенджер Telegram"""
    def messenger_telegram(self):
        with allure.step("Messenger Telegram"):
            Logger.add_start_step(method='messenger_telegram')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.click_telegram_button()
            time.sleep(2)
            self.assert_url("https://ohota26.ru/")
            Logger.add_end_step(url=self.driver.current_url, method='messenger_telegram')

    """Переход в мессенджер Vk"""
    def messenger_vk(self):
        with allure.step("Messenger VK"):
            Logger.add_start_step(method='messenger_vk')
            self.get_current_url()
            self.assert_url("https://ohota26.ru/")
            self.click_vk_button()
            time.sleep(2)
            self.assert_url("https://ohota26.ru/")
            Logger.add_end_step(url=self.driver.current_url, method='messenger_vk')

