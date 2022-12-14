from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.foxnews.com/")


class FoxNewsArticle:
    topic = ""
    title = ""
    link = ""

"testing change"
def FoxNewsPrint():
    ListOfThings = FoxNewsScrape()

    for i in ListOfThings:
        print(f"Topic: {i.topic}\n{i.title}\nLink: {i.link}\n")


def FoxNewsHeadline():
    Headline = FoxNewsArticle
    Headline.topic = "HEADLINE"
    Headline.title = driver.find_element(By.XPATH,
                                         "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[1]/div/article/div[2]/header/h2/a").get_attribute(
        "textContent")  # HeadLine Article
    Headline.link = driver.find_element(By.XPATH,
                                        "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[1]/div/article/div[2]/header/h2/a").get_attribute(
        "href")  # HeadLine Link

    return Headline


def FoxNewsScrape():
    Articles = []
    Articles.append(FoxNewsHeadline())

    ExclusiveClipsSection = len(driver.find_elements(By.XPATH,
                                                     "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div[3]/section/div/article")) + 1
    HeadlineClipsSection = len(
        driver.find_elements(By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[3]/div/article")) + 1

    driver.execute_script("window.scrollTo(0,3000)")

    for i in range(1, HeadlineClipsSection):
        HeadlineClips = FoxNewsArticle()
        HeadlineClips.topic = "HEADLINE"
        HeadlineClips.title = driver.find_element(By.XPATH,
                                                  "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[3]/div/article[{}]/div[2]/header/h2/a".format(
                                                      i)).get_attribute("textContent")
        HeadlineClips.link = driver.find_element(By.XPATH,
                                                 "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div/div[3]/div/article[{}]/div[2]/header/h2/a".format(
                                                     i)).get_attribute("href")

        Articles.append(HeadlineClips)
    for i in range(1, ExclusiveClipsSection):
        ExclusiveClips = FoxNewsArticle()
        try:
            ExclusiveClips.topic = driver.find_element(By.XPATH,
                                                       "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div["
                                                       "3]/section/div/article[{}]/div[2]/header/div/span/a".format(
                                                           i)).get_attribute("textContent").upper()
        except:
            ExclusiveClips.topic = "N/A"

        ExclusiveClips.title = driver.find_element(By.XPATH,
                                                   "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div["
                                                   "3]/section/div/article[{}]/div[2]/header/h2/a".format(
                                                       i)).get_attribute("textContent")
        ExclusiveClips.link = driver.find_element(By.XPATH,
                                                  "//*[@id='wrapper']/div/div[2]/div[1]/aside[1]/div/div/div["
                                                  "3]/section/div/article[{}]/div[2]/header/h2/a".format(
                                                      i)).get_attribute("href")
        Articles.append(ExclusiveClips)

    return Articles

def testingCode():
    driver.execute_script("window.scrollTo(0,3000)")

    ExtraArticles = driver.find_elements(By.XPATH, "//div[@class='collection collection-article-list']//div[@class='content article-list']//child::article")

    for i in range(1, len(ExtraArticles)):
        print(ExtraArticles[i].find_element(By.XPATH, "//div[@class='collection collection-article-list']//div[@class='content article-list']//article[contains(@class, 'article story-{}')]//div[@class='m']//a".format(i)).get_attribute('href'))

testingCode()
#FoxNewsPrint()
driver.close()
