from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Initialize the Chrome driver using ChromeDriverManager to automatically download the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to a webpage (Google homepage as an example)
driver.get("https://www.novatr.com")

# Print "Hello World" in the console
print("Hello World")

# Close the browser after the operation
driver.quit()
