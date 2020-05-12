from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome("C:/Users/ysatish/PycharmProjects/all rules/driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.myntra.com/men-tshirts")
chali = driver.find_elements_by_xpath('//li//a[1]//div[2]//div[1]//span')
dak = driver.find_elements_by_xpath('//li//a[1]//div[2]//div[1]//span[1]')
sub = len(chali)
da = len(dak)
print(da)
print(sub)
for i in range(0, sub):


        frs = chali[i].text

        print(frs)

















