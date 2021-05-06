import openpyxl as openpyxl
from selenium import webdriver
import xlrd
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://imgadm.wdf.global.corp.sap:3061/")
driver.find_element_by_xpath("//a[contains(text(),'Deployment')]").click()
driver.find_element_by_xpath("//a[contains(text(),'QA Mode')]").click()


print(driver.title)
path = "C:\Python files\Cdata.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb.active
Val= sheet.cell(2,2).value
driver.find_element_by_id("MainPlaceHolder_tbxUserId").send_keys(Val)
driver.find_element_by_id("contentframe").click()

driver.find_element_by_id("MainPlaceHolder_tbxEquipmentNumber").send_keys("1234567890")
#driver.find_element_by_id("MainPlaceHolder_tbxEquipmentNumber").click()

driver.find_element_by_id("contentframe").click()
Select(driver.find_element_by_name("ctl00$MainPlaceHolder$ddlRegion")).select_by_value("AMER")
Select(driver.find_element_by_id("MainPlaceHolder_ddlLocation")).select_by_value("Newtown Square")
driver.find_element_by_id("MainPlaceHolder_rbtType_3").click()
Select(driver.find_element_by_id("MainPlaceHolder_ddlInstance")).select_by_value("E")
driver.find_element_by_id("MainPlaceHolder_tbxMacAddress").send_keys("00:50:56")
driver.find_element_by_name("ctl00$MainPlaceHolder$tbxMacAddress").send_keys(":86:4a:b0")
Select(driver.find_element_by_id("MainPlaceHolder_ddlOSCollection")).select_by_value("7a8a238d-e590-495f-8dbb-3b740b5d3e06")
driver.find_element_by_id("MainPlaceHolder_chkEmailToUser").click()
driver.find_element_by_id("MainPlaceHolder_chkEmailToOperator").click()
driver.find_element_by_id("MainPlaceHolder_btnContinue").click()


