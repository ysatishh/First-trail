from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("C:/Users/ysatish/PycharmProjects/all rules/driver/chromedriver.exe")
driver.get('https://www.myntra.com/shop/men')
action = ActionChains(driver)
cha = driver.find_element_by_xpath("//a[contains(text(),'Men')]")
action.move_to_element(cha).perform()
fdf = driver.find_element_by_xpath("//a[contains(text(),'Topwear')]")
assert fdf.text == 'Topwear'
print(fdf.text)
fdf.click()
driver.back()   #this return to previous page


####-------IGNOR---------------##
#owl = driver.find_element_by_xpath('//*[@id="sortable-results"]/ul/li/a')
#size = len(driver.find_elements_by_xpath('//*[@id="sortable-results"]/ul/li/a'))
#print(size)
#for i in range(0, size):
   # owl = driver.find_elements_by_xpath('//*[@id="sortable-results"]/ul/li/p/a')
    #owl[i].click()
    #driver.find_element_by_xpath('/html/body/section/header/nav/ul/li[3]/p/a').click()