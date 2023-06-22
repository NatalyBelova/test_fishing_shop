import time
from telnetlib import EC

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


def test_buy_product(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    lp = Login_page(driver)  # Авторизация
    lp.authorisation()

    udp = User_data_page(driver) # Страница с данными пользователя
    udp.select_main_page()

    mp = Main_page(driver) # Главная страница
    mp.select_menu()

    pp = Products_page(driver) # Страница с продуктами
    pp.select_products()

    cp = Cart_page(driver) # Страница корзины
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.client_information()



    print("Finish Test")
    time.sleep(5)
    driver.quit()





