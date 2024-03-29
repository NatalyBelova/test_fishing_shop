import time
from telnetlib import EC

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.products_page import Products_page
from pages.user_data_page import User_data_page

"""Расширенное тестирование. Проверка верной работы строки поиска по слову Ласты"""
@allure.description("Test product search 1")
def test_product_search_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    lp = Login_page(driver)                  # Авторизация
    lp.authorisation()

    udp = User_data_page(driver)             # Страница с данными пользователя
    udp.select_main_page()

    mp = Main_page(driver)                   # Главная страница
    mp.search_1()

    print("Finish Test")
    time.sleep(5)
    driver.quit()

"""Расширенное тестирование. Проверка верной работы строки поиска по слову Блесна"""
@allure.description("Test product search 2")
def test_product_search_2(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    lp = Login_page(driver)                  # Авторизация
    lp.authorisation()

    udp = User_data_page(driver)             # Страница с данными пользователя
    udp.select_main_page()

    mp = Main_page(driver)                   # Главная страница
    mp.search_2()

    print("Finish Test")
    driver.quit()

"""Расширенное тестирование. Проверка верной работы строки поиска по слову Лодка"""
@allure.description("Test product search 3")
def test_product_search_3(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    lp = Login_page(driver)                  # Авторизация
    lp.authorisation()

    udp = User_data_page(driver)             # Страница с данными пользователя
    udp.select_main_page()

    mp = Main_page(driver)                   # Главная страница
    mp.search_3()

    print("Finish Test")
    time.sleep(5)
    driver.quit()





