# use this file for ABU SAQUIB interview


# Scenario:

# You need to write a Selenium-based automated test in JAVA to verify the functionality of a login form on a web application. The login page has the following elements:
# A username input field with the ID username.
# A password input field with the ID password.
# A submit button with the ID login-btn.
# A login error message with the class error-msg, which appears when the credentials are incorrect.

# The test needs to:
# Launch the application.
# Enter valid credentials and check for successful login (verify the presence of a dashboard element, #dashboard).
# Enter invalid credentials and verify that the error message appears.

# Question:
# Write the JAVA code using Selenium to automate this scenario, including appropriate wait conditions, error handling, and any assumptions you need to make (e.g., valid credentials).

Response:package Demo;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Example4 {



	public void OrangeHRM() {



		WebDriverManager.chromedriver().setup();

		WebDriver driver = new ChromeDriver();

		driver.manage().window().maximize();

		try {

		driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
		driver.manage().timeouts().implicitlyWait(10,Duration.ofSeconds(10));

		String ErrorMessage="Invalid credentials";

		WebElement Username= driver.findElement(By.xpath("//input[@name='username']"));
		WebElement Pass= driver.findElement(By.xpath("//input[@name='password']"));
		WebElement Login= driver.findElement(By.xpath("//button[@type='submit']"));
		WebElement ErrorMess= driver.findElement(By.xpath("//p[text()='Invalid credentials']"));


		Username.sendKeys("Admin");

		Pass.sendKeys("Admin12");

		Login.click();


		WebDriverWait wait= new WebDriverWait(10,Duration.ofSeconds(seconds));

		wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//p[text()='Invalid credentials']")));

		if(ErrorMess.getText().equals(ErrorMessage)) {

			Assert.assertEquals(true, false);
			System.out.println("Error Massage is showing");

		}

		else {
		}

		}




		catch(Exception e) {

			e.printStackTrace();
		}
		finally{

			driver.close();

		}
	}


}




