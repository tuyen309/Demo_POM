def validate_text(driver, xpath, expected_text):
    element_text = driver.find_element(By.XPATH, xpath).text
    return element_text == expected_text
