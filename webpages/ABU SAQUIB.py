# use this file for ABU SAQUIB interview


# Scenario:
# Elements on the login page:
# A username input field with the ID username.
# A password input field with the ID password.
# A submit button with the ID login-btn.
# A login error message with the class error-msg, which appears when the credentials are incorrect.

# Test Requirements:
# Launch the application.
# Enter valid credentials and check for a successful login (verify the presence of a dashboard element with the ID #dashboard).
# Enter invalid credentials and verify that the error message appears.

Response:

# package Demo;

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




