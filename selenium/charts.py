from selenium import webdriver

# setup the driver
driver = webdriver.Chrome()
driver.get('https://url-to-the-page.com')

# Use JavaScript to fetch chart data
result = driver.execute_script("return Chart.instances[0].data;")
print(result)  # This should print data used by the chart

# Now you can assert values in `result` to validate the chart