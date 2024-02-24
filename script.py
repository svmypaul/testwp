from selenium import webdriver
import time
import streamlit as st
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

dv = driver.get("https://web.whatsapp.com")

time.sleep(15)
element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[3]/div/span')
element.click()

time.sleep(5)
number = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/form/input')
number.send_keys("7679735335")

time.sleep(5)
enterbtn = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div[3]/div[2]/button')
enterbtn.click()

time.sleep(5)
getcode = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div')
getcode.text
textcode = getcode.text
string_without_newlines = textcode.replace('\n', '')

print(string_without_newlines)
st.write(string_without_newlines)
