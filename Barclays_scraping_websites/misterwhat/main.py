from selenium_operations import initialize_driver, click_element, send_keys_to_element
import pandas as pd
from data_processing import serialize_to_json
import time
from selenium.webdriver.common.by import By


def scrape_misterwhat(post_code_list):
    driver = initialize_driver()
    dd = {}
    for postcode in post_code_list[:10]:
        print(postcode)
        url = f"https://www.misterwhat.co.uk/search?what=Farmers&where={postcode}"
        driver.get(url)

        selector11 = '//*[@id="cat"]/section/div[1]/div[3]/ul/li'
        elems = driver.find_elements(By.XPATH, selector11)
        print(len(elems))
        dict_country = {}
        if len(elems) < 1:
            elem = driver.find_elements(By.CSS_SELECTOR, 'a.compName')
            print(len(elem))
            total_element = len(elem)
            name = []
            website = []
            address1 = []
            address2 = []
            address3 = []

            for i in range(2, total_element+2):
                selector = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/a'
                elem = driver.find_element(By.XPATH, selector)

                name.append(elem.text)
                elem = driver.find_element(By.XPATH, selector)

                website.append(elem.get_attribute('href'))
                xpath_name1 = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/span/span[1]'
                elem = driver.find_element(By.XPATH, xpath_name1)

                address1.append(elem.text)
                xpath_name2 = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/span/span[2]'
                elem = driver.find_element(By.XPATH, xpath_name2)

                address2.append(elem.text)
                xpath_name3 = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/span/span[3]'
                elem = driver.find_element(By.XPATH, xpath_name3)

                address3.append(elem.text)
            time.sleep(3)
            dict_country[str(1)] = {'name': name, 'website': website, 'address1': address1, 'address2': address2,
                                     'address3': address3}
        else:

            for k in range(1, len(elems)):
                print("page", k)
                uu = f'&page={k}'
                final_url = url + uu
                driver.get(final_url)
                time.sleep(3)
                elem = driver.find_elements(By.CSS_SELECTOR, 'a.compName')
                print(len(elem))
                total_element = len(elem)
                name = []
                website = []
                address1 = []
                address2 = []
                address3 = []

                for i in range(2, total_element+2):
                    selector = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/a'
                    elem = driver.find_element(By.XPATH, selector)

                    name.append(elem.text)
                    elem = driver.find_element(By.XPATH, selector)

                    website.append(elem.get_attribute('href'))
                    xpath_name1 = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/span/span[1]'
                    elem = driver.find_element(By.XPATH, xpath_name1)

                    address1.append(elem.text)
                    xpath_name2 = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/span/span[2]'
                    elem = driver.find_element(By.XPATH, xpath_name2)

                    address2.append(elem.text)
                    xpath_name3 = f'//*[@id="cat"]/section/div[1]/div[2]/div[{i}]/div/div[1]/span/span/span[3]'
                    elem = driver.find_element(By.XPATH, xpath_name3)

                    address3.append(elem.text)
                time.sleep(3)
                dict_country[str(k)] = {'name': name, 'website': website, 'address1': address1, 'address2': address2,
                                         'address3': address3}
        dd[postcode] = dict_country
    driver.quit()
    return dd


if __name__ == "__main__":
    df1 = pd.read_csv("postcodes.csv")
    post_code_list = df1['postcode'].to_list()
    dd = scrape_misterwhat(post_code_list)
    serialize_to_json(dd, "misterwhat_farm.json")
