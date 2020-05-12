from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:/Users/ysatish/PycharmProjects/all rules/driver/chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(0)
action = ActionChains(driver)
source_element = driver.find_element_by_xpath("//p[text()='Drag me to my target']")
dest_element = driver.find_element_by_id("droppable")
action.drag_and_drop(source_element, dest_element).perform()
#--successfully tested--- -#