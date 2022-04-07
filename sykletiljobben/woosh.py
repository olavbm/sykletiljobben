import arrow
import time
from selenium import webdriver
import auth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.sykletiljobben.no/workouts/training")

elem = driver.find_element(By.ID, "email")
elem.click()
elem.send_keys("om@safebase.no")

elem = driver.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-success.pull-right')
elem.click()

elem = driver.find_element(By.ID, 'password')
elem.send_keys(auth.secret_pass)

elem = driver.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.pull-right")
elem.click()

elem = driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block")
elem.click()

# slow rendering times
time.sleep(3)

elem = driver.find_element(By.ID, "registerActivityId")
elem.click()

time.sleep(1)

ActionChains(driver).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

time.sleep(1)

elem = driver.find_element(By.ID, "DateOfRegisterActivity")
elem.send_keys(str(arrow.now().date()))

