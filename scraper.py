import os
import time
import requests
import selenium
import time
import io
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException



# Install driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# specify search url
q = input("Value you want to search")
search_url = "https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"          #the images will be copyright-free images
driver.get(search_url.format(q=q))

def scroll_to_end(driver):
    # scroll to the end of page
    driver.execute_script('window.scrollTo(0, document.body.scrillHeight);')
    # sleep between interactions
    time.sleep(5)

# locate the images to be scrapped from the current page
imgResults = driver.find_elements(by=By.XPATH, value="//img[contains(@class,'Q4LuWd')]")

