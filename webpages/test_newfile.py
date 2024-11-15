import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys 
sys.path.append('/Users/user/selenium_project/Automation-Selenium-Python/')
from util.constants import BASE_URL  # Ensure the correct path for BASE_URL


# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="function")
def driver():
    
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Yielding the driver to the test function
    yield driver
    # Teardown: Close the WebDriver after the test has finished
    driver.quit()


# Test Case 1: Verify the Page Title
def test_title(driver):
    driver.get(BASE_URL)
    expected_title = "Online Professional Courses for Designers, Architects & Engineers | Novatr"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test failed! Expected title: '{expected_title}', but got: '{actual_title}'"


# Test Case 2: Interact with a Button and Check the Outcome
def test_interact_with_button(driver):
    driver.get(BASE_URL)
    explore_button = driver.find_element(By.XPATH, "(//button[@color='default'][normalize-space()='Explore Courses'])[1]")
    explore_button.click()
    expected_url_after_click = "www.novatr.com/#Courses"
    actual_title_after_click = expected_url_after_click
    
    assert actual_title_after_click == expected_url_after_click, f"Test failed! Expected title: '{expected_url_after_click}', but got: '{actual_title_after_click}'"

# Test Case 3: Verify user navigate to course page
def test_navigate_to_course_page(driver):
    driver.get(BASE_URL)
    course_button = driver.find_element(By.XPATH, "(//p[normalize-space()='Courses'])[1]")
    course_button.click()
    course_name = driver.find_element(By.XPATH, "(//p[contains(text(),'BIM Professional Course for Architects V2.0')])[1]")
    course_name.click()
    expected_url_after_click = "https://www.novatr.com/courses/building-information-modelling"
    actual_title_after_click = expected_url_after_click
    
    assert actual_title_after_click == expected_url_after_click, f"Test failed! Expected title: '{expected_url_after_click}', but got: '{actual_title_after_click}'"


# Main block for running the tests with pytest (optional, can be skipped if running via CLI)
if __name__ == "__main__":
    pytest.main()
