# Flight Search Automation Script - Goibibo
# Website-testing-selenium

## Overview
This script automates the process of searching for flights on the Goibibo website using Selenium WebDriver. It performs tasks such as searching for flights, applying filters for 1-stop flights within a specific price range, verifying filtered results, extracting relevant flight data, and saving the data to an Excel file.

## Requirements
- **Python 3.x**  
- **Selenium**  
- **Pandas**  
- **Openpyxl**  
- **Chrome WebDriver** (Ensure that the appropriate version is installed and the path is correctly set in the script)

## To install the required Python packages:
```bash
pip install selenium pandas openpyxl
```
## Setup Instructions
1. Install Selenium WebDriver

Download and install ChromeDriver to automate the Chrome browser:

    Download the appropriate version of ChromeDriver based on your Chrome version from ChromeDriver Downloads.
    Ensure the path to chromedriver is correctly set in the script.

2. Setting Up the Script

    Update the executable_path='/path/to/chromedriver' with the location where you have saved your chromedriver executable.

3. Ensure you have the necessary Python libraries installed:

    Selenium: This is the library used for browser automation.
    Pandas: Used for saving the flight data into an Excel file.
    Openpyxl: Required for writing data to Excel files.
```bash
pip install selenium pandas openpyxl
```

## Script Breakdown
1. Search Flights

    The search_flights function takes the from_location, to_location, and departure_date as input and automates the flight search on Goibibo.
    The script interacts with the search bar elements and enters the respective location and date.

2. Apply Filters

    The apply_filters function applies the following filters:
        Flight stops: The script selects the filter for "1 Stop" flights.
        Price range: Set a price range (default: ₹4000 to ₹8000). This can be customized via the function parameters.

3. Verify Filtered Flights

    The verify_filtered_flights function verifies that all the displayed flights are 1-stop flights by checking the "Stop" information in the search results.

4. Extract Flight Data

    The extract_flight_data function scrapes the flight details such as the flight company, price, and the route (from-to) for each flight that matches the applied filters.

5. Save Data to Excel

    The save_to_excel function converts the extracted flight data into a Pandas DataFrame and saves it into an Excel file named flight_data.xlsx.

## Example Usage

To search for flights from Delhi to Mumbai on 2025-01-10 with a price range between ₹4000 and ₹8000, simply run the script.

from_location = "Delhi"
to_location = "Mumbai"
departure_date = "2025-01-10"

search_flights(from_location, to_location, departure_date)
apply_filters(min_price=4000, max_price=8000)
verify_filtered_flights()
flight_data = extract_flight_data()
save_to_excel(flight_data)

## This will:

    Open the Goibibo website.
    Search for flights between Delhi and Mumbai on the given date.
    Apply filters for 1-stop flights and price range.
    Verify that only 1-stop flights appear.
    Extract flight details (company, price, and from-to).
    Save the extracted data into an Excel file called flight_data.xlsx.

## File Output

    The script will generate an Excel file (flight_data.xlsx) containing the following columns:
        Flight Company: The name of the airline or flight company.
        Price: The price of the flight.
        From - To: The route details (departure and destination cities).

## Troubleshooting

    If you face issues related to elements not being found or timeouts, increase the time.sleep() intervals in the script to give the page more time to load elements.
    Ensure the correct version of chromedriver is being used to match your version of Chrome.

## License

This project is open-source and released under the MIT License. Feel free to modify and improve the script according to your needs.
