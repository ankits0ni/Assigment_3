from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the Canadian Tire website
driver.get("https://www.canadiantire.ca/en.html")

# Click on the "Hot Sale" link
hot_sale_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/promotions/hot-sale.html']"))
)
hot_sale_link.click()

# Wait for the specific product link to be clickable
product_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/pdp/hoover-onepwr-emerge-jumpstart-cordless-stick-vacuum-kit-0437100p.html#srp']"))
)
product_link.click()

# Wait for the "Add to Cart" button to be clickable and click it
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart"))
)
add_to_cart_button.click()

# Wait for the "Continue to Cart" button to be clickable and click it
continue_to_cart_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "footer-btn"))
)
continue_to_cart_button.click()


# Close the webdriver
driver.quit()
