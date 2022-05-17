from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
# Add experimental options to force chromedriver to not close chrome tab instantly
chrome_options.add_experimental_option("detach", True)
# Add experimental options to remove "Google Chrome is controlled by automated software" notification
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# You can change this into any link you want
driver.get("https://www.google.com")
