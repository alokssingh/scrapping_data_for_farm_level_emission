from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def initialize_driver():
    options = Options()
    options.add_argument('--headless=new')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def navigate_to_page(driver, url):
    driver.get(url)


def click_element(driver, xpath):
    elem = driver.find_element(By.XPATH, xpath)
    elem.click()


def send_keys_to_element(driver, xpath, keys):
    elem = driver.find_element(By.XPATH, xpath)
    elem.send_keys(keys)