import os
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


os.environ['PATH'] += r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.arminvestmentcenter.com/Account/Login')
driver.implicitly_wait(10)

username = ''
password = ''

# login
driver.find_element(By.ID, "Username").send_keys(username)
driver.find_element(By.ID, "Password").send_keys(password)
driver.find_element(By.CLASS_NAME, "after").click()

# close security warning
driver.find_element(By.XPATH, "//button[text()[normalize-space()='Okay']]").click()

# navigate to transaction history
driver.find_element(By.XPATH, "(//span[text()='Mutual Fund Account'])[2]").click()
driver.find_element(By.XPATH, "(//a[@href='/Client/Portfolio/AccountStatement'])[2]").click()

driver.find_element(By.XPATH, "//div[@class='footer-disc']/following-sibling::div[1]").click()

# pick date
driver.find_element(By.ID, "endDate").click()
endDate = driver.find_element(By.XPATH, "//td[@data-title='r2c4']").click()

driver.find_element(By.ID, "startDate").click()
startDdate = driver.find_element(By.XPATH, "//td[@data-title='r2c1']").click()

# select transactions type
tranType = driver.find_element(By.ID, "TransactionType")
tranDrop = Select(tranType)

tranDrop.select_by_visible_text("Redemption")

driver.find_element(By.XPATH, "//span[text()='View Transactions']").click()

# close active browser
driver.quit()
