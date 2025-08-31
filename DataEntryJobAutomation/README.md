# Zillow Scraper & Google Form Automation

This Python project scrapes real estate data from a Zillow clone website and automatically submits the data to a Google Form. After submission, it saves all the submitted data into an Excel file (`submitted_data.xlsx`) for record-keeping.

---

## Features

- Scrapes property **addresses**, **prices**, and **links** from a Zillow clone website.
- Automatically fills out and submits a **Google Form** for each property.
- Saves all submitted data into an **Excel file**.
- Handles multiple submissions and clicks "Submit another response" for continuous automation.
- Built using Python, Selenium, BeautifulSoup, and OpenPyXL.

---

## Technologies Used

- **Python** – main programming language.
- **Requests** – to fetch the web page.
- **BeautifulSoup** – for parsing HTML and extracting data.
- **Selenium** – to interact with Google Forms dynamically.
- **OpenPyXL** – to create and write to Excel files.
- **Regex (re)** – to clean and format price data.

---

## How It Works

1. Fetches the Zillow clone page using `requests` and parses it with `BeautifulSoup`.
2. Extracts **addresses**, **prices**, and **links** of properties.
3. Opens the Google Form using `Selenium` and fills in each field.
4. Submits the form and saves the submitted data to `submitted_data.xlsx`.
5. Repeats for all properties in the list.

---

## What I Learned

- How to **scrape data** from websites using BeautifulSoup.
- How to **automate browser actions** (form filling, button clicks) using Selenium.
- How to **store data in Excel** dynamically with OpenPyXL.
- How to **integrate multiple Python libraries** in one project for automation tasks.
- Best practices for **waiting for page elements** to load with `WebDriverWait`.


