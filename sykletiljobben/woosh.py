from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.sykletiljobben.no/workouts/training")
elem = driver.find_element(By.Id, "registerActivityBtn")
elem.click()
