import requests                   # To fetch the webpage
from bs4 import BeautifulSoup      # To parse HTML content
import re                          # For regular expressions (cleaning price strings)
from selenium import webdriver     # To automate browser actions
from selenium.webdriver import ActionChains  # To simulate mouse/keyboard actions
from selenium.webdriver.common.by import By  # To locate elements
from selenium.webdriver.support.wait import WebDriverWait  # To wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Conditions for waiting
from openpyxl import Workbook      # To create and write to Excel files
import time                        # To pause execution for a few seconds


# URL of the site with property listings
url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)  # Fetch the webpage content

# Parse the HTML content
soup = BeautifulSoup(response.text,"html.parser")

# Extract all property addresses
addresses = soup.find_all("address", attrs={"data-test": "property-card-addr"})
address_list = []
for a in addresses:
    address_list.append(a.text.strip())  # Clean text and add to list
print(address_list)

# Extract all property prices
prices = soup.find_all("span", attrs={"data-test": "property-card-price"})
price_list = []
for p in prices:
    clean_price = re.split(r"[+/]", p.text)[0]  # Remove extra characters after + or /
    price_list.append(clean_price)
print(price_list)

# Extract all property links
links = soup.find_all("a", attrs={"data-test": "property-card-link"})
href_list = []
for link in links:
    href_list.append(link['href'])  # Get the href attribute
print(href_list)


# Set Chrome options so browser doesn't close automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keep browser open after script ends

# Open Google Form in Chrome
driver = webdriver.Chrome(options=options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeQuimqOCaOqJWVP1GYGPDPGraAHTtCciYqS8epfCBxp2N0Tg/viewform?usp=header")

wait = WebDriverWait(driver, 10)  # Set up wait for elements to load

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.append(["Address", "Price", "Link"])  # Add headers to the Excel sheet


# Loop through all properties and submit data
for i in range(len(address_list)):
    # Wait until input fields are loaded
    all_inputs = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.whsOnd.zHQkBf"))
    )

    # Assign the input fields
    address_input = all_inputs[0]
    price_input = all_inputs[1]
    link_input = all_inputs[2]

    # Enter address
    ActionChains(driver).move_to_element(address_input).click().perform()
    address_input.send_keys(address_list[i])

    # Enter price
    ActionChains(driver).move_to_element(price_input).click().perform()
    price_input.send_keys(price_list[i])

    # Enter link
    ActionChains(driver).move_to_element(link_input).click().perform()
    link_input.send_keys(href_list[i])

    # Click the Submit button
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']/.."))
    )
    submit_btn.click()

    # Save the submitted data to Excel
    ws.append([address_list[i], price_list[i], href_list[i]])
    wb.save("submitted_data.xlsx")  # Save after each entry to prevent data loss

    time.sleep(2)  # Wait for 2 seconds before submitting another

    # Click "Submit another response" to continue the loop
    another_response = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response"))
    )
    another_response.click()
    time.sleep(1)  # Short pause to allow form to reset
