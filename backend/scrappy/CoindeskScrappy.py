from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import csv

class CoindeskScrappy:
    def __init__(self):
        self.site_url = "https://www.coindesk.com/coindesk-news/"
        self.site_name = "Coindesk"
        self.driver = webdriver.Firefox()  # or Chrome(), or any other browser

    def get_html(self):
        try:
            self.driver.get(self.site_url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            # Extract the news articles from the initial page
            articles = soup.find_all('article')
            data = []
            for article in articles:
                # Extract the title, link, and other relevant information
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                text = f"{title} {link}"
                data.append({'text': text, 'source': self.site_name})

            # Find the "Show more" button and click it
            show_more_button = self.driver.find_element_by_css_selector('.Button__ButtonBase-sc-1sh00b8-0.Button__ContainedButton-sc-1sh00b8-3.gjtbfz.keIoOV')
            show_more_button.click()

            # Wait for the page to load and then extract the new articles
            self.driver.implicitly_wait(5)  # adjust the wait time as needed
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            articles = soup.find_all('article')
            for article in articles:
                # Extract the title, link, and other relevant information
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                text = f"{title} {link}"
                data.append({'text': text, 'source': self.site_name})

            # Save the data to a CSV file
            with open('coindesk_news.csv', 'w', newline='') as csvfile:
                fieldnames = ['text', 'source']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.driver.quit()

scraper = CoindeskScrappy()
scraper.get_html()