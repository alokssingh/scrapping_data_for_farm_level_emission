from selenium_operations import initialize_driver, click_element, get_element_text
from data_processing import process_data, save_results_to_excel
from collections import defaultdict
import time


if __name__ == "__main__":
    df = pd.read_excel("RP_Cleaned.xlsx")
    df = df[['owner_name', 'owner_address_1', 'owner_postcode']]
    data = df
    abc = process_data(df)

    driver = initialize_driver()

    name1 = []
    address1 = []
    business1 = []

    for city in abc[:5]:
        place = city
        url = f'https://directory.independent.co.uk/farming-mixed/in/{place}'
        print(url)
        driver.get(url)

        try:
            XPATH_COOKIES = '//*[@id="onetrust-reject-all-handler"]'
            click_element(driver, XPATH_COOKIES)
        except Exception as err:
            pass

        xpath_check_element = '//*[@id="list"]/div/div[1]/div/div'
        elems = driver.find_elements(By.XPATH, xpath_check_element)

        for i in range(1, len(elems) - 1):
            xpath_1 = f'//*[@id="list"]/div/div[1]/div/div[{i}]/div/div/div/div/h2/a'
            xpath_2 = f'//*[@id="list"]/div/div[1]/div/div[{i}]/div/div/div/div/p[1]'
            xpath_3 = f'//*[@id="list"]/div/div[1]/div/div[{i}]/div/div/div/div/p[3]'
            print(get_element_text(driver, xpath_1))
            name1.append(get_element_text(driver, xpath_1))
            business1.append(get_element_text(driver, xpath_2))
            address1.append(get_element_text(driver, xpath_3))

        for k in range(2, 11):
            print(f'https://directory.independent.co.uk/farming-mixed/in/{place}?page={k}')
            driver.get(f'https://directory.independent.co.uk/farming-mixed/in/{place}?page={k}')
            elems1 = driver.find_elements(By.XPATH, xpath_check_element)
            for ii in range(1, len(elems1) - 1):
                xpath_1 = f'//*[@id="list"]/div/div[1]/div/div[{ii}]/div/div/div/div/h2/a'
                xpath_2 = f'//*[@id="list"]/div/div[1]/div/div[{ii}]/div/div/div/div/p[1]'
                xpath_3 = f'//*[@id="list"]/div/div[1]/div/div[{ii}]/div/div/div/div/p[3]'
                name1.append(get_element_text(driver, xpath_1))
                business1.append(get_element_text(driver, xpath_2))
                address1.append(get_element_text(driver, xpath_3))
            time.sleep(5)

        data = {
            'name1': name1,
            'business1': business1,
            'address1': address1
        }
        save_results_to_excel(data, place)

    driver.quit()
