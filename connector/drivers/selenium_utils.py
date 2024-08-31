from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def find_element_presence(driver: webdriver.Firefox, 
                          xpath: str,
                          delay: int = 30,
                          is_quit: bool = False):

    elem = None

    try:
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print("Found Element:", xpath)

    except (NoSuchElementException, TimeoutException):
        if is_quit:
            driver.quit()
        else:
            pass

    return elem


def find_element_clickable(driver: webdriver.Firefox, 
                          xpath: str,
                          delay: int = 30,
                          is_quit: bool = False):

    elem = None

    try:
        elem = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        print("Found Element:", xpath)

    except (NoSuchElementException, TimeoutException):
        if is_quit:
            driver.quit()
        else:
            pass

    return elem

