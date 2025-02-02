from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scrape_table_data(driver, xpath):
    elements = driver.find_elements(By.XPATH, xpath)
    return [ele.text for ele in elements]


def scrape_postcodes(driver, xpath):
    elements = driver.find_elements(By.XPATH, xpath)
    return [ele.text for ele in elements]


def click_next_button(driver, xpath, page_no):
    if page_no == 1:
        next_button_click = xpath
    else:
        next_button_click = f'{xpath}[2]'
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_click)))
    elem.click()
    time.sleep(2)