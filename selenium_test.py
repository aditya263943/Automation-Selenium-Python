from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Initialize the Chrome driver using ChromeDriverManager to automatically download the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to a webpage (Google homepage as an example)
driver.get("https://www.novatr.com")

# Perform basic interactions like finding an element
title = "Online Professional Courses for Designers, Architects & Engineers | Novatr"
print("Title of the page is:", title)

# Close the browser after the operation
driver.quit()
