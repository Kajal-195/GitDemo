import time

import control as control
from selenium.common.exceptions import NoAlertPresentException


from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('prefs', {'safebrowsing.enabled': True})
opts.add_argument('--safebrowsing-disable-download-protection')
driver = webdriver.Chrome(options=opts)

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://sapprinting.wdf.sap.corp:1080/printer.aspx")
print(driver.title)

driver.find_element_by_id("__item0-container-sapprinting---locations--Tree-1-expander").click()
driver.find_element_by_id("__item0-container-sapprinting---locations--Tree-6-expander").click()
driver.find_element_by_id("__item0-container-sapprinting---locations--Tree-8-expander").click()
driver.find_element_by_id("__item0-container-sapprinting---locations--Tree-17-content").click()
driver.find_element_by_id("__button4-container-sapprinting---location--printerTable-1-BDI-content").click()
driver.find_element_by_id("__mbox-btn-0-content").click()
time.sleep(5)
driver.get("chrome://downloads/")
driver.find_element_by_xpath("/html/body/downloads-manager//div[2]/iron-list/downloads-item//div[2]/div[2]/div[5]/div[2]/cr-button").click()

if control.get_attribute(“attributename”)==”attributeValue”:




