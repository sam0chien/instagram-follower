import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

load_dotenv()
CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH']
SIMILAR_ACCOUNT = os.environ['SIMILAR_ACCOUNT']
INS_USERNAME = os.environ['INS_USERNAME']
INS_PASSWORD = os.environ['INS_PASSWORD']


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        sleep(2)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')

        username.send_keys(INS_USERNAME)
        password.send_keys(INS_PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(4)
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        sleep(2)
        search.send_keys(Keys.ENTER)
        sleep(1.5)
        search.send_keys(Keys.ENTER)
        sleep(4)
        followers = self.driver.find_element_by_css_selector('a.-nal3')
        followers.click()

    def follow(self):
        sleep(2)
        f_body = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 5:
            self.driver.execute_script('arguments[0].scrollTop = '
                                       'arguments[0].scrollHeight;',
                                       f_body)
            sleep(1)
            scroll += 1
            if scroll == 4:
                follows = self.driver.find_elements_by_css_selector("li button")
                for follow in follows:
                    try:
                        follow.click()
                        sleep(0.5)
                    except ElementClickInterceptedException:
                        # unfollow = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
                        # unfollow.click()
                        cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                        cancel.click()
                        sleep(0.5)
                scroll = 0
            continue


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

# Unfollow

# driver = webdriver.Chrome(executable_path='/Users/poppopgd/Development/chromedriver')
#
# driver.get('https://www.instagram.com/accounts/login/')
# sleep(2)
# username = driver.find_element_by_name('username')
# password = driver.find_element_by_name('password')
#
# username.send_keys(INS_USERNAME)
# password.send_keys(INS_PASSWORD)
# password.send_keys(Keys.ENTER)
# sleep(4)
#
# driver.get('https://www.instagram.com/sampythontest666/')
# sleep(5)
#
# following_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
# following_button.click()
# sleep(1)
# f_body = driver.find_element_by_xpath("//div[@class='isgrP']")
# scroll = 0
# while scroll < 5:
#     driver.execute_script('arguments[0].scrollTop = '
#                           'arguments[0].scrollHeight;',
#                            f_body)
#     sleep(1)
#     scroll += 1
#     if scroll == 4:
#         followings = driver.find_elements_by_css_selector("li button")
#         for following in followings:
#             if following.text == 'Following':
#                 following.click()
#                 sleep(0.5)
#                 unfollow = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
#                 unfollow.click()
#                 sleep(0.5)
#             else:
#                 pass
#         scroll = 0
#     continue
