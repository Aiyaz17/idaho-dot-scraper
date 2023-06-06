from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium.webdriver.chrome.options import Options


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('log-level=3')
    driver = webdriver.Chrome(options=chrome_options)

    return driver

def scrape(url,driver,wait):
    driver.get(url)

    # Wait for the table to load
    table_loaded = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#table_id tbody")))
    # Find the clickable elements and click on them
    top_5_rows = table_loaded.find_elements(By.TAG_NAME,"tr")  # First 5 rows
    return top_5_rows

def extract_functions(rows):
    subpages_functions = []
    count = 0
    for row in rows:
        if count == 5:
            break
        link = row.find_element(By.TAG_NAME, "a")
        if link.get_attribute("onclick") is not None:
            subpages_functions.append(link.get_attribute("onclick"))
            count += 1
    return subpages_functions


def scrape_individual_pages(driver,wait,subpages_functions):
    data=[]
    for subpage_function in subpages_functions:
        currpage_data = {
            "quest_id": re.search(r'prevnext\((\d+)\)', subpage_function).group(1),
        }
        
        driver.execute_script(subpage_function)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table")))
        time.sleep(1)

        posting_header = driver.find_element(By.CLASS_NAME, "posting-second-header")

        # Find the <b> tag within the element with text "Closing date"
        closing_date_tag = posting_header.find_element(By.XPATH, ".//b[contains(text(), 'Closing Date')]")
    
        currpage_data["closing_date"] = closing_date_tag.text.split(":")[1].strip()

        est_value_notes_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Est. Value Notes:')]/following-sibling::td").text
        description_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Description:')]/following-sibling::td").text
        currpage_data["est_value_notes"] = est_value_notes_element
        currpage_data["description"] = description_element
        data.append(currpage_data)
    
    return data



if __name__ == '__main__':
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
    top_5_rows = scrape(url,driver,wait)
    subpages_functions = extract_functions(top_5_rows)
    data = scrape_individual_pages(driver,wait,subpages_functions)
    print(data)
