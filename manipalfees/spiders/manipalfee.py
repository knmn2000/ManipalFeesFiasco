from os.path import abspath, dirname, join

import scrapy
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path_dir = dirname(abspath(__file__))
geckodriver_path = abspath(join(path_dir, "./../chromedriver"))


class manipalFeeBot(scrapy.Spider):
    name = "manipalfeebot"
    keywords = None

    def start_requests(self):
        url = "https://twitter.com/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_argument("window-size=1200x600")

        driver = webdriver.Chrome(chrome_options=options)
        action = ActionChains(driver)
        driver.get("https://twitter.com/")
        print("PRESS C WHEN YOU ARE ON THE HASHTAG's PAGE")
        import pdb

        pdb.set_trace()
        retweets = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='retweet']",))
        )
        retweets = driver.find_elements_by_xpath("//div[@data-testid='retweet']")
        elem = driver.find_element_by_xpath(
            "//div[@class='css-1dbjc4n r-16y2uox r-1wbh5a2 r-1pi2tsx r-1777fci']"
        )
        driver.execute_script(
            "var element = arguments[0]; element.parentNode.removeChild(element);", elem
        )
        while True:
            for retweet in retweets:
                try:
                    retweet.click()
                    driver.find_element_by_xpath(
                        '//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div'
                    ).click()
                except:
                    pass
            retweets = driver.find_elements_by_xpath("//div[@data-testid='retweet']")
