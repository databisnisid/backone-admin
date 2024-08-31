from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.conf import settings
from connector.drivers import pop3
from time import sleep


def get_quota(username: str = settings.DSC_USERNAME, password: str = ''):

    quota_current = ''
    quota_total = ''
    quota_day = ''

    if username is not None and password is not None:

        print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        if settings.REMOTE_SELENIUM:
            #driver_options = webdriver.ChromeOptions()
            driver_options = webdriver.FirefoxOptions()

            driver = webdriver.Remote(
                command_executor=settings.SELENIUM_DOCKER,
                options=driver_options
            )
        else:
            driver = webdriver.Firefox()

        # Delete All Cookies ?
        #driver.delete_all_cookies()

        driver.get("https://dsc.telkomsel.com")
        delay = 10

        """ Sending Username """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='mobileNumberOrEmail']"))
            )

            elem.send_keys(username)
            elem.send_keys(Keys.RETURN)

        except (NoSuchElementException, TimeoutException):
            driver.quit()

        """ Check Term and Condition """
        try:
            elem = WebDriverWait(driver, delay).until(
                    EC.presence_of_element_located((By.XPATH, 
                                                    "//input[@id='acceptTnc']"))
                    )

            elem.click()

        except (NoSuchElementException, TimeoutException):
            driver.quit()

        """ Click GET CODE Button """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))
            )

            elem.click()

        except (NoSuchElementException, TimeoutException):
            driver.quit()

        """ 
        Create Function to get Code from email
        Use poplib 
        """
        print("Napping for 30 seconds...") 
        sleep(30)
        otp_code = pop3.get_otp_code()
        print("OTP Code:", otp_code)

        """ Enter CODE """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='otp']"))
            )

            elem.send_keys(otp_code)

        except (NoSuchElementException, TimeoutException):
            driver.quit()

        """ SUBMIT """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
            )

            elem.click()

        except (NoSuchElementException, TimeoutException):
            driver.quit()

        """ Get Quota Information """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.ID, "package-meter-chart"))
            )
            quota_current = elem.find_element(By.XPATH, "./div[2]/div[2]/div[1]").text
            quota_total = elem.find_element(By.XPATH, "./div[2]/div[2]/div[3]").text
            elem = driver.find_element(By.XPATH, "//div[text()='Internet Orbit']")
            quota_day = elem.find_element(By.XPATH, "./span").text
        except (NoSuchElementException, TimeoutException):
            pass

        driver.quit()

    return quota_current, quota_total, quota_day
