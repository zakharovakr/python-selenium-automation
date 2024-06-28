# logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# Email field
driver.find_element(By.XPATH, "//input[@type='email']")
# Continue button
driver.find_element(By.ID, 'continue')
# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# Need help link
driver.find_element(By.XPATH, "//span[contains(text(), 'help')]")
# Forgot your password link
driver.find_element(By.XPATH, "//a[contains(text(), 'password')]")
# Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[contains(text(), 'issues')]")
# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
