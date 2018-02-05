from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
base_url = driver.get("http://www.python.org")

assert "Python" in driver.title

el = driver.find_element_by_name("q")
el.clear()
el.send_keys("pycon")
el.send_keys(Keys.RETURN)

assert "No results" not in driver.page_source
driver.close()

