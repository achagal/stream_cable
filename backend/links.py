import bs4
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# scrape netflix to create a set of links to click through 
# write those links onto an empty txt file


# handle log in page
# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Netflix login page
driver.get("https://www.netflix.com/login")

try:
    # Wait for the email input field to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-uia="login-field"]'))
    )

    # Locate and fill in the email input field
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[data-uia="login-field"]')
    email_field.send_keys("mus@chagal.net")

    # Wait for the password input field to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-uia="password-field"]'))
    )

    # Locate and fill in the password input field
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[data-uia="password-field"]')
    password_field.send_keys("eachagal1")

    # Wait for the login button to be clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-uia="login-submit-button"]'))
    )

    # Locate and click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-uia="login-submit-button"]')
    login_button.click()

    # Wait for login to complete
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "profile-icon"))
    )

    print("Login successful!")

except Exception as e:
    # If the email input field is not found, assume we are already logged in
    print("Already logged in or login page not found.")



try:
    # Wait for profile selection page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.choose-profile'))
        )

        # Select the first profile
        profile_link = driver.find_element(By.CSS_SELECTOR, 'ul.choose-profile li.profile a.profile-link')
        profile_link.click()

        # Wait for the main Netflix page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "profile-icon"))
        )
        print("Successfully chose a profile and are in Netflix home page")
except Exception as e:
    print("A profile has already been chosen")


# now that the web scraper is on main page
# navigate to genres button in top left
# get a set of links that the second script will use

# navigate to tv shows page, then get the link for every genre




