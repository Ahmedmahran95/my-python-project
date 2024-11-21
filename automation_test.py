from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from time import sleep  # Optional for pausing between actions (not recommended for production)

# Replace with your desired browser driver path
driver_path = "path/to/your/chromedriver"

# Set up the browser driver
driver = webdriver.Chrome()

try:
    # Open the Magento demo website
    driver.get("https://magento.softwaretestingboard.com/")
    sleep(1)
    
    # Click on "Create an Account" link
    create_account_link = driver.find_element(By.LINK_TEXT, "Create an Account")
    create_account_link.click()

    sleep(1)
    
    # Fill out the account creation form (replace with your desired details)
    first_name_field = driver.find_element(By.ID, "firstname")
    first_name_field.send_keys("Ahmed")

    sleep(1)
    
    last_name_field = driver.find_element(By.ID, "lastname")
    last_name_field.send_keys("yahia")

    sleep(1)
    
    email_field = driver.find_element(By.ID, "email_address")
    email_field.send_keys("Ahmed2002@gmail.com")

    sleep(1)
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Ahmedmahran95@")

    sleep(1)
    
    password_confirmation_field = driver.find_element(By.ID, "password-confirmation")
    password_confirmation_field.send_keys("Ahmedmahran95@")

    sleep(3)
    
    # 
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action.submit.primary"))
    ).click()

    sleep(1)
    

    # Navigate to the Home page
    driver.get("https://magento.softwaretestingboard.com/")

   # Wait for the page to load and ensure the "Add to Compare" button is visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='action tocompare']")))

    # Wait for 3 seconds (adjust as needed)
    sleep(3)

    # First iteration: Find and click the first "Add to Compare" button for product 158
    first_add_to_compare_button = driver.find_element(By.XPATH, "//a[@class='action tocompare' and contains(@data-post, 'product\":\"158')]")
    driver.execute_script("arguments[0].scrollIntoView();", first_add_to_compare_button)
    sleep(1)  # Wait a moment to ensure the button is visible
    driver.execute_script("arguments[0].click();", first_add_to_compare_button)  # Click the button
    print("First product (product 158) added to compare.")

    # Scroll down once more
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)  # Wait for scroll to finish

    # Second iteration: Find and click the second "Add to Compare" button for product 6
    second_add_to_compare_button = driver.find_element(By.XPATH, "//a[@class='action tocompare' and contains(@data-post, 'product\":\"6')]")
    driver.execute_script("arguments[0].scrollIntoView();", second_add_to_compare_button)
    sleep(1)  # Wait a moment to ensure the button is visible
    driver.execute_script("arguments[0].click();", second_add_to_compare_button)  # Click the button
    print("Second product (product 6) added to compare.")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    sleep(30 * 1)
    # Close the browser window
    driver.quit()