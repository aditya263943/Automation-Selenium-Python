Test Cases:

Scope:
There is a User Profile page in an application, where user put his/her Aadhar number and click on submit button, the submit button invokes Aadhar API and fetch user details and display as table. On the click on Submit Button a spinner will appear that should go away the moment details are displayed.
No authentication is required.

Please right down the test cases for the same?

Solution:

"There is a User Profile page in an application, where user put his/her Aadhar number and click on submit button, the submit button invokes Aadhar API and fetch user details and display as table. On the click on Submit Button a spinner will appear that should go away the moment details are displayed.
No authentication is required.



Verify if the Aadhar number field must accept only numeric values and not alphanumeric
Verify if only 12 digits are acceptable
Verify if user is not allowed to enter any negative value
Verify if error alert is shown to the user if any incorrect value is entered.
Verify if aadhar number accepts spaces
Verify if the field is not accepting all 0's
Verify if the field is not accepting all any special characters
Verify if the system shows message to user if aadhar number is not correct, or the data does not exist on the database
Verify if the user is able to click submit button and details are fetched in single click.
Verify if the same form works similarly on other browser similarly.


Verify if user is getting all the personal details based on aadhar number entered
Verify if the aadhar number is not masked, and should be completely visible.
Verify if the user name has first and last name in proper casing
Verify if the issue date is correctly mentioned.
Verify if the dob is mentioned in correct date format
Verify if the phone number fetched has 10 digits along with country code
Verify if the correct address is fetched along with pin code of the user
Verify if the spinner is not present if all the fetched details are visible to the user
Verify if the details are fetched in less time and spinner is not shown now.
Verify if the success message is shown to the user after correct details are fetched.
Verify if decimal values are not accepted in the form.




# Task 1: Automate Google Search
# Description:
# Write a Selenium WebDriver script to:

# Open https://www.google.com.
# Search for the term "Selenium WebDriver".
# Verify that the search results page displays results related to "Selenium WebDriver" by checking the page title or URL.
# Expected Output:

# The script should navigate to Google, perform the search, and validate that the results are relevant.


Solution:
"/******************************************************************************

Online
Java
Compiler.
Code, Compile, Run and Debug
java
program
online.
Write
your
code in this
editor and press
""
Run
""
button
to
execute
it.

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /

public


class Main
    public
    static
    void
    main(String[]
    args){
        System.setProperty(""
    webdriver.chrome.driver
    "".
    ""
    path
    "");

    WebDriver
    driver = new
    ChromeDriver(driver);

    driver.get(""
    https: // www.google.com
    "");
    WebElement
    searchbox = driver.findElement(By.Id(""
    id
    ""));
    searchbox.sendKeys(""
    Selenium
    WebDriver
    "");
    WebElement
    searchbtn = driver.findElement(By.Id(""
    id
    ""));
    searchbtn.click();

    String
    currentUrl = driver.getCurrentUrl();
    System.out.print(""
    url
    "" + currentUrl);

    String
    expectedUrl = ""
    test
    "";
    Asset.assertEquals(currentUrl, expectedUrl);
    }
    }

    / *



# Task 2: Verify Broken Links
# Description:
# Write a Selenium WebDriver script to:

# Open https://the-internet.herokuapp.com/broken_images.
# Find all the links on the page.
# Check if each link is working by verifying the HTTP status code.
# Expected Output:

# The script should log all the URLs along with their status codes and highlight any broken links (status code >= 400).

Solution: