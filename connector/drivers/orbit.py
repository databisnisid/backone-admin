from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.conf import settings
import logging


# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# def get_quota(username='budithegreat09@gmail.com', password='Failover6!'):
def get_quota(username, password):

    quota_current = ""
    quota_total = ""
    quota_day = ""

    if username is not None and password is not None:

        # print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        logging.info(f"Use Selenium Server: {settings.REMOTE_SELENIUM}")
        if settings.REMOTE_SELENIUM:
            # driver_options = webdriver.ChromeOptions()
            # driver_options = webdriver.FirefoxOptions()
            options = Options()
            options.add_argument(f"--proxy-server={settings.PROXY_SERVER}")

            driver = webdriver.Remote(
                # command_executor=settings.SELENIUM_DOCKER, options=driver_options
                command_executor=settings.SELENIUM_DOCKER,
                options=options,
            )
        else:
            driver = webdriver.Firefox()

        # Delete All Cookies ?
        # driver.delete_all_cookies()

        driver.get("https://www.myorbit.id/login")
        delay = 10

        """ Sending Username """
        try:
            #            elem = WebDriverWait(driver, delay).until(
            #                EC.presence_of_element_located((By.XPATH, "//input[contains(@label,'Alamat Email/No. HP')]"))
            #            )
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='']"))
            )
            #            elem = WebDriverWait(driver, delay).until(
            #                EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1cwyjr8"))
            #            )
            elem.send_keys(username)
            elem.send_keys(Keys.RETURN)
        except (NoSuchElementException, TimeoutException):
            driver.quit()

        logging.info("Sending username succeed")

        """ Sending Password """
        try:
            #            elem = WebDriverWait(driver, delay).until(
            #                EC.presence_of_element_located((By.XPATH, "//input[contains(@label,'Password')]"))
            #            )
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='']"))
            )
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)
        except (NoSuchElementException, TimeoutException):
            driver.quit()

        logging.info("Sending password succeed")

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

        logging.info(f"Get information {quota_current}, {quota_total}, {quota_day}")

    return quota_current, quota_total, quota_day
