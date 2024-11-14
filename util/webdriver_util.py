from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver():
    """Initialize and return the WebDriver instance"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver
