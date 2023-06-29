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

"""Расширенное тестирование. Проверка перехода на мессенеджер WhatsApp"""
@allure.description("Test messenger WhatsApp")
def test_messenger_whats_app(set_up):
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
    mp.messenger_whats_app()

    print("Finish Test")
    time.sleep(2)
    driver.quit()

"""Расширенное тестирование. Проверка перехода на мессенеджер Telegram"""
@allure.description("Test messenger Telegram")
def test_messenger_telegram(set_up):
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
    mp.messenger_telegram()

    print("Finish Test")
    time.sleep(2)
    driver.quit()

"""Расширенное тестирование. Проверка перехода на мессенеджер VK"""
@allure.description("Test messenger VK")
def test_messenger_vk(set_up):
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
    mp.messenger_vk()

    print("Finish Test")
    time.sleep(2)
    driver.quit()





