from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_website(url, element_selector, expected_text):
    # Setup the Chrome WebDriver
    driver = webdriver.Chrome(
        executable_path='path/to/chromedriver')  # Modify with the correct path to your ChromeDriver

    try:
        # Launch the specified URL
        driver.get(url)

        # Wait until the element is located using explicit wait
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element_selector))
        )

        # Get the text of the found element
        actual_text = element.text

        # Assert condition: Check if the actual text of the element matches expected text
        assert expected_text in actual_text, f"Expected text not found. Expected: {expected_text}, Found: {actual_text}"

        print("Test passed: Element contains expected text.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

# Example usage