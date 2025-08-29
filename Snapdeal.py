from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
Servi_obj = Service(r"C:\drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Servi_obj)
driver.maximize_window()
driver.get("https://www.snapdeal.com")

# Verify URL
expected_url = "https://www.snapdeal.com/"
current_url = driver.current_url

if expected_url == current_url:
    print("Test Passed: Correct Snapdeal URL opened.")
else:
    print(f"Test Failed: Expected {expected_url} but got {current_url}")

# Click to sign in
driver.find_element(By.XPATH, "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]/div/span[2]/i").click()
time.sleep(2)

# Click to login user
driver.find_element(By.XPATH, "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/span[2]").click()

# Switch to iframe for login
wait = WebDriverWait(driver, 10)
iframe = wait.until(EC.presence_of_element_located((By.ID, "loginIframe")))
driver.switch_to.frame(iframe)

# Enter user email
email_field = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
email_field.send_keys("sudama89840@gmail.com")

driver.find_element(By.ID, "checkUser").click()

# Enter OTP
otp_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginOtpUC']/div[1]/input")))
otp_field.send_keys("2004")  # Dummy OTP

driver.find_element(By.ID, "loginUsingOtp").click()

# Switch back to main content
driver.switch_to.default_content()

# ---- Product Search ----
search_box = wait.until(EC.presence_of_element_located((By.ID, "inputValEnter")))
search_box.send_keys("shoes")
search_box.submit()

# Category navigation (Men → Sports Shoes)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='js-4583-nav']/li[1]/a/div[1]"))).click()

# Select a product 
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='659177333667']/div[2]/div[1]/a/p"))).click()

# Switch to new product window
driver.switch_to.window(driver.window_handles[1])

# Select shoes size
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='attribute-select-1']/div[2]/div/div/div[6]/div/div"))).click()

# Add to cart
wait.until(EC.element_to_be_clickable((By.ID, "add-cart-button-id"))).click()

# View Cart
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[1]/div/i"))).click()

# Remove product from cart
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rtbScriptContainer']/div[5]/ul/li/div[8]/div/span"))).click()

# Proceed to checkout
wait.until(EC.element_to_be_clickable((By.ID, "rzp-quickcart-button"))).click()

print("Test Completed Successfully.")
time.sleep(5)
driver.quit()

