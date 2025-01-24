from selenium import webdriver
from selenium.webdriver.common.by import By

# Path to Brave browser executable
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Windows example



# Path to Brave's user data directory
user_data_dir = "C:/Users/Omarm/AppData/Local/BraveSoftware/Brave-Browser/User Data"  # Windows example

# Set up Brave options
options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
import time
# Open Upwork notifications page
driver.get("https://www.upwork.com/ab/notifications/")

# Wait for the page to load
time.sleep(10)  # Adjust sleep time if necessary

# Function to click "X" on all notifications
def close_new_job_notifications():
    try:
        # Find all notification rows
        notifications = driver.find_elements(By.CSS_SELECTOR, 'div.notification-row')
        for notification in notifications:
            # Check if the notification contains the text "New job"
            if "New job" in notification.text:
                # Find the "X" button within the notification and click it
                close_button = notification.find_element(By.CSS_SELECTOR, 'button[title="Remove notification"]')
                close_button.click()
                time.sleep(1)  # Add a small delay to avoid overwhelming the page
    except Exception as e:
        print(f"Error closing notifications: {e}")

# Close notifications on the first page

# Click "View more" to load additional notifications
while True:
    try:
        close_new_job_notifications()

        view_more_button = driver.find_element(By.CSS_SELECTOR, 'button.air3-btn-tertiary')
        view_more_button.click()
        time.sleep(3)  # Wait for new notifications to load

    except Exception as e:
        print(f"Error clicking 'View more': {e}")
        break

# Wait for a few seconds before closing the browser
time.sleep(5)

# Close the browser
driver.quit()