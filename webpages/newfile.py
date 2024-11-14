import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from constants import BASE_URL  # Import the constant

class TestNovatrPage(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver using ChromeDriverManager to automatically download the driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_title(self):
        # Navigate to the webpage using the BASE_URL constant
        self.driver.get(BASE_URL)
        
        # Define the expected title
        expected_title = "Online Professional Courses for Designers, Architects & Engineers | Novatr"
        
        # Get the actual title of the page
        actual_title = self.driver.title
        
        # Assert that the actual title matches the expected title
        self.assertEqual(actual_title, expected_title, f"Test failed! Expected title: '{expected_title}', but got: '{actual_title}'")
        
        # If the test passes, this will be printed
        print("Test passed! The page title is correct.")

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

# # Run the tests
# if __name__ == "__main__":
#     unittest.main()