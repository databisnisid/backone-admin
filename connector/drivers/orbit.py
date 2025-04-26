from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.conf import settings
import logging
from time import sleep
import connector.drivers.selenium_utils as sutils


# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def driver_start():
    # print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
    logging.info(f"Use Selenium Server: {settings.REMOTE_SELENIUM}")
    if settings.REMOTE_SELENIUM:
        # driver_options = webdriver.ChromeOptions()
        # driver_options = webdriver.FirefoxOptions()
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--proxy-server={settings.PROXY_SERVER}")

        driver = webdriver.Remote(
            # command_executor=settings.SELENIUM_DOCKER, options=driver_options
            command_executor=settings.SELENIUM_DOCKER,
            options=options,
        )
    else:
        driver = webdriver.Chrome()

    return driver


def driver_quit(driver):
    driver.quit()


# def get_quota(username='budithegreat09@gmail.com', password='Failover6!'):
def get_quota(username, password, driver):

    quota_current = ""
    quota_total = ""
    quota_day = ""
    error_msg = ""

    if username is not None and password is not None:

        # print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        """
        logging.info(f"Use Selenium Server: {settings.REMOTE_SELENIUM}")
        if settings.REMOTE_SELENIUM:
            # driver_options = webdriver.ChromeOptions()
            # driver_options = webdriver.FirefoxOptions()
            options = Options()
            # options.add_argument("--headless")
            options.add_argument(f"--proxy-server={settings.PROXY_SERVER}")

            driver = webdriver.Remote(
                # command_executor=settings.SELENIUM_DOCKER, options=driver_options
                command_executor=settings.SELENIUM_DOCKER,
                options=options,
            )
        else:
            driver = webdriver.Firefox()
        """

        # Delete All Cookies ?
        # driver.delete_all_cookies()

        logging.info("Go to login page")
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

        """ Check for pop up """

        # elem = sutils.find_element_clickable(
        elem = sutils.find_element_presence(
            driver, "/html/body/div[1]/div[2]/div[5]/div/div[2]/div/div", delay, False
        )

        if elem:
            # logging.info("Ada pop up Error!")
            try:
                elem.click()
            except WebDriverException or StaleElementReferenceException:
                pass

        """ Ensure go to dasboard """

        sleep(delay / 2)
        logging.info("Go to Dashboard")
        driver.get("https://www.myorbit.id/dashboard")

        """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div/p[contains(text(), 'Mengerti')]")
                )
            )

            logging.info("Ada pop up Mengerti!")
            elem.click()

        except (NoSuchElementException, TimeoutException):
            pass
        """

        """ Get Quota Information """

        """ Find aktif s.d """
        elem = sutils.find_element_presence(
            driver,
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/p[contains(text(), 'aktif s.d')]",
            delay,
            False,
        )

        if elem:
            logging.info(f"{elem.text}")
            quota_day = elem.text

            logging.info("MSISDN is OK -> Continue")

            """ START - Find Quota Current """
            elem = sutils.find_element_presence(
                driver,
                "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/p[1]",
                delay,
                False,
            )

            if elem:
                logging.info(f"{elem.text}")
                quota_current = elem.text.replace(" ", "")
            """ END - Find Quota Current """

            """ START - Find Quota Total """
            elem = sutils.find_element_presence(
                driver,
                "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/p[2]",
                delay,
                False,
            )

            if elem:
                logging.info(f"{elem.text}")
                quota_total = elem.text.replace("/", "").replace(" ", "")
            """ END - Find Quota Total """

            logging.info(f"{quota_current}/{quota_total} {quota_day}")

        else:
            """Get Error Message"""
            elem = sutils.find_element_presence(
                driver,
                "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/p",
                delay,
                False,
            )

            if elem:
                error_msg = elem.text
                logging.info(error_msg)

        """ Click Button Profil"""

        """
        elem = sutils.find_element_clickable(
            driver, "//*[@id='btn-profile']", delay, False
        )

        if elem:
            logging.info("Click Button Profile")

            try:
                elem.click()
            except WebDriverException or StaleElementReferenceException:
                pass

        sleep(3)
        """

        """ Try to logout here """

        """
        elem = sutils.find_element_clickable(
            # driver, "//div/div/p[contains(text(), 'Keluar')]", delay, False
            driver,
            "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[9]",
            delay,
            False,
        )

        if elem:
            logging.info("Logout!")

            try:
                elem.click()
            except WebDriverException or StaleElementReferenceException:
                pass

        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div/div/p[contains(text(), 'Keluar')]")
                )
            )

            elem.click()

        except (NoSuchElementException, TimeoutException):
            pass

        """
        # driver.quit()
        # logging.info(f"Sleeping {delay} seconds")
        # sleep(delay)

        # logging.info(f"Get information {quota_current}, {quota_total}, {quota_day}")

    return quota_current, quota_total, quota_day
