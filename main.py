# Import necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import selenium.webdriver.support
from selenium.webdriver.firefox.service import  Service
from selenium.webdriver.support.ui import WebDriverWait
import time
#from selenium.webdriver.sinchsms import SinchSMS

# Create a Firefox WebDriver instance
driver: WebDriver = webdriver.Firefox()

# Navigate to a webpage
driver.get('https://hubtel.com/')

# Maximize the browser window
driver.maximize_window()

# Pause execution for 5 seconds
time.sleep(5)

# Navigate to another webpage 'https://explore.hubtel.com/schools/'
driver.get('https://explore.hubtel.com/schools/')
# Pause execution for 5 seconds
time.sleep(5)

# Click on an element identified by XPath on the webpage
driver.find_element(By.XPATH,"/html/body/div[5]/div/div[1]/div/div/div[1]/div/div/a").click()
# Pause execution for 10 seconds
time.sleep(10)

# Click on another element identified by XPath on the webpage
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/section/div/div[2]/div/div/a").click()
# Pause execution for 10 seconds
time.sleep(10)

# Enter a mobile number in the input field identified by XPath
driver.find_element(By.XPATH,"//input[@placeholder='Your mobile number']").send_keys('0244536448')
time.sleep(10)

# Enter a mobile number in the input field identified by XPath
driver.find_element(By.XPATH,"//div[@class='pt-4']").click()
# Pause execution for 20 seconds
time.sleep(20)


# Enter a mobile number in the input field identified by XPath
driver.find_element(By.XPATH, "//a[@id='otp-submit']").click()
# Pause execution for 20 seconds
time.sleep(20)


# Enter a mobile number in the input field identified by XPath
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/a").click()
# Pause execution for 20 seconds
time.sleep(10)

# Close the browser window and end the WebDriver session
driver.quit()