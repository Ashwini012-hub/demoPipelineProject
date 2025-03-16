import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    """Set up the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def navigate_to_site(driver, url):
    """Navigate to the specified URL."""
    driver.get(url)


def drag_and_drop_within_iframe(driver, iframe_selector, drag_selector, drop_selector):
    """Perform drag and drop action within an iframe."""
    try:
        # Wait for the iframe to be available and switch to it
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, iframe_selector))
        )

        # Wait for draggable and droppable elements to be visible
        draggable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, drag_selector))
        )
        droppable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, drop_selector))
        )

        # Create ActionChain to perform drag and drop
        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()

        print("Drag and drop action inside iframe has been performed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Switch back to default content
        driver.switch_to.default_content()


def quit_driver(driver):
    """Close the WebDriver."""
    driver.quit()


if __name__ == '__main__':
    # Initialize the WebDriver and navigate to the web page
    driver = setup_driver()
    navigate_to_site(driver, "https://the-internet.herokuapp.com/drag_and_drop")

    # Perform drag and drop within an iframe
    drag_and_drop_within_iframe(driver, "iframe_selector", "#column-a", "#column-b")

    # Clean up by closing the WebDriver
    quit_driver(driver)