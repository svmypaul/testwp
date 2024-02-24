import streamlit as st
from selenium import webdriver
import time
driver = webdriver.Chrome()
dv = driver.get(URL)

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

st.write(string_without_newlines)
