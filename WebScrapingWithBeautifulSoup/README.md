# Web Scraping with BeautifulSoup - Top 100 Movies

This project demonstrates how to perform web scraping using Python and BeautifulSoup.  
The goal of this project was to extract the **titles and rankings of the top 100 movies** from a movie website and save the results into a text file for easy reference and further use.

---

## Project Overview

Web scraping is a powerful technique for collecting data from websites automatically.  
In this project, I used the `requests` library to fetch the web page content and `BeautifulSoup` to parse the HTML and extract the relevant information.  
The extracted movie titles are stored in reverse order to match the original ranking, and then saved into a `movies.txt` file.

---

## Features

- Fetch web page content from an archived movie website
- Parse HTML using BeautifulSoup
- Extract movie titles and their ranking order
- Save the results into a text file for easy access

---

## Requirements

- Python 3.x  
- `requests` library  
- `beautifulsoup4` library  

Install the required libraries using pip if you don’t have them already:

```bash
pip install requests beautifulsoup4
