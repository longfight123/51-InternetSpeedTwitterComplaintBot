from selenium import webdriver
import time
import os
from dotenv import load_dotenv

load_dotenv('.env')
CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PW = os.getenv('TWITTER_PW')

class InternetSpeedTwitterBot:
    """
    A class used to control the browser to send complaints via twitter.

    ...

    Attributes
    ----------
    driver: WebDriver
        a tool for automated testing of webapps
    down: int
        the promised download speed from user's service provider
    up: int
        the promised upload speed from the user's service provider

    Methods
    -------
    get_internet_speed()
        goes on the internet to obtain the user's upload and download speeds
    tweet_at_provider()
        goes to twitter using the user's account to send a tweet
        to your service provider with your current upload and download speeds
    """

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """goes on the internet to obtain your upload and download speeds
        """

        self.driver.get('https://speedtest.net')
        time.sleep(5)
        go_element = self.driver.find_element_by_css_selector('.speedtest-container .start-button .js-start-test')
        go_element.click()
        time.sleep(45)
        down_speed_element = self.driver.find_element_by_css_selector('.result-data .download-speed')
        self.down = down_speed_element.text
        up_speed_element = self.driver.find_element_by_css_selector('.result-data .upload-speed')
        self.up = up_speed_element.text
        print(self.down)
        print(self.up)


    def tweet_at_provider(self):
        """goes to twitter using the user's account to send a tweet
        to your service provider with your current upload and download speeds
        """

        self.driver.get('https://twitter.com')
        time.sleep(3)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login_button.click()
        time.sleep(3)
        username_element = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input')
        username_element.send_keys(TWITTER_EMAIL)
        password_element = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-iphfwy.r-s1qlax.r-ttdzmv > div > input')
        password_element.send_keys(TWITTER_PW)
        login_button = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div')
        login_button.click()
        time.sleep(5)
        text_area_element = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-18jsvk2.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
        text_area_element.send_keys(f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up')
        tweet_button = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(4) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-19u6a5r.r-ero68b.r-1gg2371.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr')
        tweet_button.click()
        time.sleep(3)
        self.driver.quit()
