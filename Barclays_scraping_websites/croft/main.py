from selenium_operations import initialize_driver, navigate_to_page, click_element, send_keys_to_element
from web_scraping import scrape_table_data, scrape_postcodes, click_next_button
import pandas as pd


def main():
    driver = initialize_driver()
    navigate_to_page(driver, 'https://www.crofts.ros.gov.uk/register/search')
    data = 'C'
    xpath_croft_input = '//*[@id="search_register_num"]'
    xpath_search_button = '//*[@id="submit_register_search"]/button[2]'
    xpath_table_data = '//*[@class="google-visualization-table-td"][4]'
    xpath_postcode = '//*[@class="google-visualization-table-td"][7]'
    xpath_next_button = '//*[@id="register_table_page_register_details"]/div/a'
    l_name = []
    postcode = []
    page_no = 1

    send_keys_to_element(driver, xpath_croft_input, data)
    click_element(driver, xpath_search_button)

    for i in range(10):
        print("page_no is: ", i)
        l_name.extend(scrape_table_data(driver, xpath_table_data))
        postcode.extend(scrape_postcodes(driver, xpath_postcode))
        click_next_button(driver, xpath_next_button, page_no)
        page_no += 1
    driver.quit()

    # Create DataFrame and save to Excel
    percentile_list = pd.DataFrame({'Croft_name': l_name, 'Postcode': postcode})
    percentile_list.to_excel("croft_scotland.xlsx", index=False)


if __name__ == "__main__":
    main()
