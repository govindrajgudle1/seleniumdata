from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\DELL\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
    print("Google Form opened successfully.")
    
    def wait_and_send_keys(xpath, keys):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element_tag = element.tag_name
        if element_tag == 'input' or element_tag == 'textarea':
            element.clear()
            element.send_keys(keys)
        else:
            driver.execute_script("arguments[0].value = arguments[1];", element, keys)
        print(f"Filled {keys} into the field with XPath {xpath}")

    wait_and_send_keys("//input[@aria-labelledby='i1']", "Govindraj Gudle")  # Full Name
    wait_and_send_keys("//input[@aria-labelledby='i5']", "1234567890")  # Contact Number
    wait_and_send_keys("//input[@aria-labelledby='i9']", "govindrajgudle33@gmail.com")  # Email ID
    wait_and_send_keys("//textarea[@aria-labelledby='i13']", "India")  # Full Address
    wait_and_send_keys("//input[@aria-labelledby='i17']", "92823")  # Pin Code
    wait_and_send_keys("//input[@aria-labelledby='i25']", "02-04-2003")  # Date of Birth
    wait_and_send_keys("//input[@aria-labelledby='i26']", "Male")  # Date of Birth



    while True:
        pass

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed and script terminated.")
