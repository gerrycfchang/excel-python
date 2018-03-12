from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome() 
browser.get("http://www.google.com")
search = browser.find_element_by_name('q')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN)
locator = (By.ID, 'pnnext')
WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(locator))
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.close()