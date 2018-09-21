from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys


driver = webdriver.PhantomJS()
print("wait a bit ...")
driver.get(sys.argv[-2])
time.sleep(2)                            #that is nessesary to load full page correctly
soup = BeautifulSoup(driver.page_source, features='html.parser')
f = open(sys.argv[-1], "wb")
f.write(soup.prettify().encode())
f.close()
driver.quit()
print("Done")
