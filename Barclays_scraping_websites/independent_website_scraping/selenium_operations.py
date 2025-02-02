from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import randint
from selenium import webdriver

WAITING_TIME = 0
RANDOM_WAITING_TIME = randint(13, 18)
SIMPLE_WAITING_TIME = randint(4, 8)
PAGE_LOAD_TIME = 60


def initialize_driver():
    options = Options()
    options.add_argument('--headless=new')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(RANDOM_WAITING_TIME)
    return driver


def click_element(driver, xpath):
    elem = WebDriverWait(driver, PAGE_LOAD_TIME).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elem.click()


def get_element_text(driver, xpath):
    elem = driver.find_element(By.XPATH, xpath).text
    return elem
