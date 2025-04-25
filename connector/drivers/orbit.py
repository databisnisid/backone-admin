from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException,
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
        # options.add_argument("--headless")
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

    if username is not None and password is not None:

        # print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        """
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
            driver = webdriver.Firefox()
        """

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

        """ Check for pop up """

        elem = sutils.find_element_clickable(
            driver, "/html/body/div[1]/div[2]/div[5]/div/div[2]/div/div", delay, False
        )

        if elem:
            # logging.info("Ada pop up Error!")
            try:
                elem.click()
            except WebDriverException:
                pass

        """ Ensure go to dasboard """

        sleep(delay / 2)
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

        elem = sutils.find_element_presence(
            driver,
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]",
            delay,
            False,
        )

        """ Find valid until """
        elem = sutils.find_element_presence(
            driver,
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/p[2]",
            delay,
            False,
        )

        if elem:
            logging.info(f"{elem.text}")
            quota_day = elem.text

        """ Find Quota Current """
        elem = sutils.find_element_presence(
            driver,
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/p[1]",
            delay,
            False,
        )

        if elem:
            logging.info(f"{elem.text}")
            quota_current = elem.text

        """ Find Quota Total """
        elem = sutils.find_element_presence(
            driver,
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/p[2]",
            delay,
            False,
        )

        if elem:
            logging.info(f"{elem.text}")
            quota_total = elem.text.replace("/", "").replace(" ", "")

        logging.info(f"{quota_current}/{quota_total} {quota_day}")

        """
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.ID, "package-meter-chart"))
            )
            quota_current = elem.find_element(By.XPATH, "./div[2]/div[2]/div[1]").text
            quota_total = elem.find_element(By.XPATH, "./div[2]/div[2]/div[3]").text
            elem = driver.find_element(By.XPATH, "//div[text()='Internet Orbit']")
            quota_day = elem.find_element(By.XPATH, "./span").text

            logging.info(f"Get information {quota_current}, {quota_total}, {quota_day}")

        except (NoSuchElementException, TimeoutException):
            pass
        """

        """ Click Button Profil"""

        logging.info("Click Button Profile")
        try:
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.ID, "btn-profile"))
            )

            elem.click()

        except (NoSuchElementException, TimeoutException):
            pass

        """ Try to logout here """
        logging.info("Logout!")

        elem = sutils.find_element_clickable(
            driver, "//div/div/p[contains(text(), 'Keluar')]", delay, False
        )

        if elem:
            elem.click()

        """
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
        logging.info(f"Sleeping {delay/2} seconds")
        sleep(delay / 2)

        # logging.info(f"Get information {quota_current}, {quota_total}, {quota_day}")

    return quota_current, quota_total, quota_day
