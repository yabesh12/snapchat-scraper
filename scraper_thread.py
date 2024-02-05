from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import re
from db import user_profile_collection
from selenium.common.exceptions import NoSuchElementException


def scrape_and_store_profile_data(url, username):
    """
    Scrape and store profile data from the provided URL.

    Args:
        url (str): The URL of the Snapchat profile.
        username (str): The username associated with the Snapchat profile.

    Returns:
        None
    """
    profile_data = {}
    try:
            
        # Configure Chrome WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        browser.implicitly_wait(5)
        time.sleep(2)

        # Use Selenium to scrape data from the provided URL
        browser.get(url)
        browser.maximize_window()

        # Extract name
        title = browser.title
        name = re.sub(r'[^a-zA-Z0-9\s]', '', title.split('(')[0].strip())
        
        # Extract category
        try:
            category_element = browser.find_element(By.XPATH, "//span[@data-testid='subCategorySection']")
            category = category_element.text if category_element else ''
        except NoSuchElementException:
            category = ''
        cleaned_category = re.sub(r'[^a-zA-Z0-9\s]', '', category)

        time.sleep(2)
        # Extract subscribers count
        try:
            subscribers_text = browser.find_element(By.XPATH, "//div[@data-testid='subscribersCountText']").text
            subscribers_count = subscribers_text.split(' ')[0]
        except NoSuchElementException:
            subscribers_count = 0

        # Extract the Address
        try:
            address = browser.find_element(By.TAG_NAME, "address").text
        except NoSuchElementException:
            address = ''


        # Store the scraped data in MongoDB
        profile_data = {
            'profile_url': url,
            'profile_username': username,
            'profile_name': name,
            'category': cleaned_category,
            'subscribers_count': subscribers_count,
            'location': address
        }

        print(profile_data)

        user_profile_collection.insert_one(profile_data)
        browser.quit()

        print("Profile data successfully uploaded!")

    except Exception as e:
        print(f"Error: {str(e)}")
