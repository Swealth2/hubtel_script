# Import necessary modules from Selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver

# Create a Firefox WebDriver instance
driver: WebDriver = webdriver.Firefox()
driver.maximize_window()

#Navigate to a webpage
driver.get('https://hubtel.com/')
# Pause script execution for 5 seconds to allow page loading
time.sleep(5)

# Navigate to a webpage
driver.get('https://explore.hubtel.com/schools/')
# Pause script execution for 10 seconds to allow page loading
time.sleep(10)

# Find image elements using XPATH
image_1 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div/div/div[1]/img')
image_2 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div/div/div[2]/img')
image_3 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div/div/div[3]/img')
image_4 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div/div/div[4]/img')
image_5 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div/div/div[5]/img')
image_6 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[1]/div/div/div[6]/img')


# Check if each image is visible and print a corresponding message
if image_1.is_displayed():
    print("The image Connecting early childhood schools to parents is visible")

else:
    print('Connecting early childhood schools to parents is not visible')


if image_2.is_displayed():
    print("The image Stay Informed is visible")
else:
    print('Stayed Informed is not visible')

if image_3.is_displayed():
    print("The image Manage PickUps is visible")
else:
    print('Manage PickUps is not visible')

if image_4.is_displayed():
    print("The image Pay School Fees")
else:
    print("Pay School Fees is not Visible")

if image_5.is_displayed():
    print("The image Manage Permission is visible")
else:
    print("Manage Permission is not visible")

if image_6.is_displayed():
    print("The image Bring Family Together")
else:
    print("Bring Family Together is not visible")

# Quit the WebDriver session
driver.quit()
