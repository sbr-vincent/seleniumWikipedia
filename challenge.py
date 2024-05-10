from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# webdriver helps us automate tasks in the browser
# Keeps Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# The driver sends the required headers to websites
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_input = driver.find_element(By.NAME, value="fName")
last_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.TAG_NAME, value="button")

first_input.send_keys("Vincent")
last_input.send_keys("G")
email_input.send_keys("coffee@gmail.com")

button.click()








