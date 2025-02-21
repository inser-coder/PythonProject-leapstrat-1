import scrapy
import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class StubHubSpider(scrapy.Spider):
    name = "stubhub_sports"

    start_urls = [
        "https://www.stubhub.com/explore?lat=MjUuNDQ3ODkwMw%3D%3D&lon=LTgwLjQ3OTIxOTY%3D&to=253402300799999&tlcId=2"
    ]

    sport_data = []

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def parse(self, response, **kwargs):
        self.driver.get(response.url)
        time.sleep(5)

        events = self.driver.find_elements(By.XPATH, "//a[contains(@class, 'hIVWQw')]")

        for event in events:
            try:
                name = event.find_element(By.XPATH, ".//p[contains(@class, 'gSA-DZE')]").text

                date = event.find_element(By.XPATH, ".//p[contains(@class,'bsWxzg')][1]").text

                place = event.find_element(By.XPATH, ".//p[contains(@class,'bsWxzg')][2]").text
                image = event.find_element(By.XPATH, ".//img[contains(@class,'fpvUjg')]").get_attribute("src")
                event_data = {
                    "name": name,
                    "date": date,
                    "location": place,
                    "image": image

                }

                self.sport_data.append(event_data)

            except Exception as e:
                self.logger.error(f"Error extracting event details: {e}")
                continue

    def closed(self, reason):
        file_path = os.path.join(os.getcwd(), "sports_data.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.sport_data, f, indent=4, ensure_ascii=False)

        self.driver.quit()