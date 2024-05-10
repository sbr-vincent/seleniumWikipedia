from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# webdriver helps us automate tasks in the browser
# Keeps Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# The driver sends the required headers to websites
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# The click function makes the driver click on a web page element that we have grabbed
# articles_count.click()

# Find element by Link Text. We look for text in a link tag that matches our value
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search_bar = driver.find_element(By.NAME, value="search")

# Sending keyboard inputs to Selenium
search_bar.send_keys("Python", Keys.ENTER)

# Quit will close the entire program
# driver.quit()
