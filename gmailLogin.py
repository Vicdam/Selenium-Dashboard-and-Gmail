import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://gmail.com')
driver.implicitly_wait(10)

Email = ''
password = ''

# login
driver.find_element(By.ID, "identifierId").send_keys(Email)
driver.find_element(By.XPATH, "//div[@id='identifierNext']").click()
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'signIn').click()

# compose and send email
driver.find_element(By.XPATH, "//div[text()='Compose']").click()

driver.find_element(By.NAME, "to").send_keys(Email)

subject = driver.find_element(By.NAME, "subjectbox")
subject.send_keys('hi,')

bodyElem = driver.find_element(By.ID, ':rg')
bodyElem.send_keys('Automation test)')

sendElem = driver.find_element(By.ID, ':q0').click()

# assert that email is received
bodyElem = driver.find_element(By.XPATH, "//span[text()='Automation test)']").click()
