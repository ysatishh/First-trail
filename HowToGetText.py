from selenium import webdriver
import time


driver = webdriver.Chrome("C:/Users/ysatish/PycharmProjects/seleniumTestwithFramework/Drivers/chromedriver.exe")
driver.get("https://www.myntra.com/men-tshirts?f=Categories%3ATshirts")
driver.find_element_by_class_name("desktop-searchBar").send_keys("bdddf")
print(driver.find_element_by_class_name("desktop-searchBar").get_attribute("value"))
driver.execute_script()
