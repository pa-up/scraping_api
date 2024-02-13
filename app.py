from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class Scraper:
    def __init__(self , browse_visually = "no"):
        self.driver = self.browser_setup(browse_visually)
        self.wait_driver = WebDriverWait(self.driver, 10)

    def browser_setup(self , browse_visually = "no"):
        """ブラウザを起動する関数"""
        options = webdriver.ChromeOptions()
        if browse_visually == "no":
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options , service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(3)
        return driver
    
    def scraping_book_off(self , searched_url):
        """ 任意のスクレイピングを実行する関数 """
        self.driver.get(searched_url)
        # self.driver.implicitly_wait(5)
        time.sleep(4)
        # html要素を取得
        week_recommend_elements = self.driver.find_element(By.CSS_SELECTOR , "section.recommend__inner").find_elements(By.CSS_SELECTOR , "div.recommend__list")
        for loop , element in enumerate(week_recommend_elements):
            if loop == 0:
                week_recommend_text = element.text
            else:
                week_recommend_text = week_recommend_text + "<br>" + element.text
        return week_recommend_text
    

class RequestData(BaseModel):
    data_list: list
    data_str: str
    data_int: int

app = FastAPI()

@app.post("/")
def cloud_fast_api(data: RequestData):
    # 呼び出し元からデータを取得
    data_list = data.data_list
    data_str = data.data_str
    data_int = data.data_int
    # スクレイピング
    searched_url = "https://shopping.bookoff.co.jp/"
    scraper = Scraper()
    week_recommend_text = scraper.scraping_book_off(searched_url)
    return {"api_output_text": week_recommend_text}