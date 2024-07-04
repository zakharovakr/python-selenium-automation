# logo
driver.find_element(By.CSS_SELECTOR, 'i[aria-label="Amazon"]')
# Create Account header
driver.find_element(By.CSS_SELECTOR, "h1")
#Your name
driver.find_element(By.ID, 'ap_customer_name')
# email
driver.find_element(By.ID, 'ap_email')
# password
driver.find_element(By.ID, 'ap_password')
# passwords must be at least 6 characters
driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least')]")
# re-enter password
driver.find_element(By.ID, 'ap_password_check')
# Create your account button / Continue button
driver.find_element(By.ID, 'continue')
# conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
# privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='register_notification_privacy_notice']")
# signin link
driver.find_element(By.CSS_SELECTOR, "a[href*='signin']")