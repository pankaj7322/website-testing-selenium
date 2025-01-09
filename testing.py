from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from openpyxl import Workbook

# Setup WebDriver (Make sure to provide the path to chromedriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open Goibibo website
driver.get('https://www.goibibo.com/flights/')

# Task 1: Perform flight search
def search_flights(from_location, to_location, departure_date):
    driver.find_element(By.ID, 'gi_search_input_source').send_keys(from_location)
    time.sleep(1)
    driver.find_element(By.ID, 'gi_search_input_source').send_keys(Keys.RETURN)
    time.sleep(1)
    
    driver.find_element(By.ID, 'gi_search_input_dest').send_keys(to_location)
    time.sleep(1)
    driver.find_element(By.ID, 'gi_search_input_dest').send_keys(Keys.RETURN)
    time.sleep(2)

    # Selecting the departure date
    date_field = driver.find_element(By.XPATH, "//input[@placeholder='Departure Date']")
    date_field.click()
    time.sleep(1)
    driver.find_element(By.XPATH, f"//div[contains(text(), '{departure_date}')]").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='PrimaryBtn makeFlex hvr-sweep-to-right']").click()
    time.sleep(5)

# Task 2: Apply filters for "1 Stop" and price range
def apply_filters(min_price=4000, max_price=8000):
    # 1 stop filter
    stop_filter = driver.find_element(By.XPATH, "//div[contains(@class,'stop-filter')]//input[@value='1']")
    if not stop_filter.is_selected():
        stop_filter.click()
    
    time.sleep(2)
    
    # Price range filter (Example: 4000 Rs to 8000 Rs)
    min_price_field = driver.find_element(By.XPATH, "//input[@placeholder='Min']")
    max_price_field = driver.find_element(By.XPATH, "//input[@placeholder='Max']")
    
    min_price_field.clear()
    min_price_field.send_keys(str(min_price))
    max_price_field.clear()
    max_price_field.send_keys(str(max_price))
    max_price_field.send_keys(Keys.RETURN)

    time.sleep(5)

# Task 3: Verify filtered flights
def verify_filtered_flights():
    flights = driver.find_elements(By.XPATH, "//div[@class='GvNdAd']//div[@class='LPNZy']")
    for flight in flights:
        stops = flight.find_element(By.XPATH, ".//span[contains(text(), 'Stop')]").text
        assert '1 Stop' in stops, f"Flight with more than 1 stop found: {stops}"

# Task 4: Extract flight data
def extract_flight_data():
    flight_data = []
    flights = driver.find_elements(By.XPATH, "//div[@class='GvNdAd']//div[@class='LPNZy']")
    for flight in flights:
        flight_company = flight.find_element(By.XPATH, ".//div[@class='cYdzjS']").text
        price = flight.find_element(By.XPATH, ".//div[@class='iXzFJr']").text
        from_to = flight.find_element(By.XPATH, ".//div[@class='LzS1Vt']").text
        flight_data.append([flight_company, price, from_to])

    return flight_data

# Task 5: Save data to Excel
def save_to_excel(flight_data):
    df = pd.DataFrame(flight_data, columns=['Flight Company', 'Price', 'From - To'])
    df.to_excel('flight_data.xlsx', index=False)

# Main workflow for Task 1
from_location = "Delhi"
to_location = "Mumbai"
departure_date = "2025-01-10"

search_flights(from_location, to_location, departure_date)
apply_filters(min_price=4000, max_price=8000)
verify_filtered_flights()
flight_data = extract_flight_data()
save_to_excel(flight_data)

driver.quit()

