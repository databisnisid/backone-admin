import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from django.conf import settings
import logging
from connector.drivers.selenium_utils import (
    find_element_presence,
    find_element_clickable,
)
from connector.drivers import pop3

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# def get_quota(username='budithegreat09@gmail.com', password='Failover6!'):
def get_quota_multi(
    username=settings.ORBIT_MULTI_USERNAME, password=settings.ORBIT_MULTI_PASSWORD
):

    quota_current = ""
    quota_total = ""
    quota_day = ""

    logging.info("Delete All Email...")
    pop3.delete_all_email(
        settings.ORBIT_MULTI_EMAIL_ADDRESS, settings.ORBIT_MULTI_EMAIL_PASSWORD
    )
    result = {}

    if username is not None and password is not None:

        # print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        logging.info(f"Use Selenium Server: {settings.REMOTE_SELENIUM}")
        if settings.REMOTE_SELENIUM:
            # driver_options = webdriver.ChromeOptions()
            # driver_options = webdriver.FirefoxOptions()

            options = Options()
            # options.add_argument("--headless")
            if settings.PROXY_SERVER:
                options.add_argument(f"--proxy-server={settings.PROXY_SERVER}")
            driver = webdriver.Remote(
                # command_executor=settings.SELENIUM_DOCKER, options=driver_options
                command_executor=settings.SELENIUM_DOCKER,
                options=options,
            )
        else:
            # driver = webdriver.Firefox()
            driver = webdriver.Chrome()
            # Use this for local SELENIUM
            # driver = webdriver.Chrome()

        # Delete All Cookies ?
        # driver.delete_all_cookies()

        url_orbit = "https://www.myorbit.id/login"
        driver.get(url_orbit)
        # driver.get("https://www.myorbit.id/login")
        delay = 10

        # Check Cookies

        elem = find_element_clickable(
            driver,
            "//*[@id='cookies1']/div/div/div[2]/div[1]/div/p[contains(text(), 'Setuju')]",
        )

        if elem:
            logging.info("Found Cookies Accept")
            elem.click()

        sleep(3)

        # print("Trying to login to ", url_orbit)
        logging.info(f"Trying to login to {url_orbit}")
        """ Sending Username """

        elem = find_element_presence(driver, "//input[@value='']")
        if elem:
            elem.send_keys(username)
            time.sleep(2)
            elem.send_keys(Keys.RETURN)

        time.sleep(3)

        otp_code = ""
        for i in range(1, 120):
            logging.info(f"Trying get code #{str(i)}")
            otp_code = pop3.get_otp_code_orbit_multi(
                settings.ORBIT_MULTI_EMAIL_ADDRESS, settings.ORBIT_MULTI_EMAIL_PASSWORD
            )
            if otp_code != "":
                print("OTP Code:", otp_code)
                logging.info(f"OTP Code: {otp_code}")
                break
            time.sleep(3)

        time.sleep(3)

        """ Find Input OTP """
        elem = find_element_presence(
            driver, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div/input[1]"
        )

        if elem:
            logging.info("Found OTP Input")
            elem.send_keys(otp_code)
        # time.sleep(300)

        """ Find button Lanjutkan """
        elem = find_element_presence(
            driver,
            "//*[@id='root']/div[5]/div[2]/div/div[2]/div[4]",
            30,
            True,
        )

        if elem:
            logging.info("Found Button Lanjutkan")
            elem.click()

        """
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
            # print("Sending Username")
            logging.info("Sending Username")
        except (NoSuchElementException, TimeoutException) as error:
            driver.quit()
            # print("Error: ", error)
            logging.info(f"Error: {error}")

        """
        """ Sending Password """
        """
        try:
            #            elem = WebDriverWait(driver, delay).until(
            #                EC.presence_of_element_located((By.XPATH, "//input[contains(@label,'Password')]"))
            #            )
            elem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='']"))
            )
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)
            # print("Sending Password")
            logging.info("Sending Password")
        except (NoSuchElementException, TimeoutException) as error:
            driver.quit()
            logging.info(f"Error: {error}")

        """
        time.sleep(60)

        """ Get Quota Multi Information """
        is_next_page = True
        page_number = 1
        # print("Login Successful. Trying to get information...")

        logging.info("Login Successful. Trying to get information...")
        while is_next_page:
            try:
                elem = WebDriverWait(driver, delay).until(
                    # EC.presence_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n']//div[contains(@class, 'css-1dbjc4n') and contains(@class, 'r-18u37iz')]"))
                    EC.presence_of_element_located(
                        # (By.XPATH, "//div[contains(text(), '628')]")
                        (By.XPATH, "//p[contains(text(), '628')]")
                    )
                )
                # logging.info(elem.text)
                logging.info(f"FOUND TOP MSISDN! {elem.text}")
                time.sleep(delay)

                logging.info("Getting table of MSISDNs")
                table_elements = driver.find_elements(
                    # By.XPATH, "//div[contains(text(), '628')]/.."
                    By.XPATH,
                    "//p[contains(text(), '628')]/..",
                )
                # logging.info(table_elements)
                # print("FOUND MSISDN!")
                # print(table_elements)
                for element in table_elements:
                    # print(element.text)
                    msisdn = element.find_element(
                        # By.XPATH, ".//div[contains(text(), '628')]"
                        By.XPATH,
                        ".//p[contains(text(), '628')]",
                    ).text
                    # print("Found MSISDN: ", msisdn)
                    logging.info(f"Found MSISDN: {msisdn}")
                    # quota = element.find_element(By.XPATH, ".//div[contains(text(), ' GB')]").text
                    # quota = element.find_element(By.XPATH, ".//div[contains(text(), 'GB')]").text
                    # print('Found Quota Info: ', quota)
                    try:
                        quota = element.find_element(
                            # By.XPATH, ".//div[contains(text(), 'GB')]"
                            By.XPATH,
                            ".//p[contains(text(), 'GB')]",
                        ).text
                        # print("Found Quota Info in GB: ", quota)
                        logging.info(f"Found Quota Info in GB: {quota}")

                    except (NoSuchElementException, TimeoutException) as error:
                        # print("Quota INFO is not FOUND! Trying again...")
                        logging.info("Quota INFO is not FOUND! Trying again...")
                        try:
                            quota = element.find_element(
                                # By.XPATH, ".//div[contains(text(), 'MB')]"
                                By.XPATH,
                                ".//p[contains(text(), 'MB')]",
                            ).text
                            # print("Found Quota Info in GB: ", quota)
                            logging.info(f"Found Quota Info in GB: {quota}")
                        except (NoSuchElementException, TimeoutException):
                            quota = "0GB / 0GB"
                            # print("Quota INFO is NOT FOUND! Set Empty: ", quota)
                            logging.info(f"Quota INFO is NOT FOUND! Set Empty: {quota}")

                    try:
                        until = element.find_element(
                            # By.XPATH, ".//div[contains(text(), 'Berlaku')]"
                            By.XPATH,
                            ".//p[contains(text(), 'Berlaku')]",
                        ).text.replace("Berlaku hingga ", "")
                        # print("Found Masa Belaku Info: ", until)
                        logging.info(f"Found Masa Belaku Info: {until}")
                    except (NoSuchElementException, TimeoutException):
                        until = None

                    result[msisdn] = [quota] + [until]
                    # print(result[msisdn])

                # page_number += 1
                try:
                    # next_page = driver.find_element(By.XPATH, "//div[contains(@style, 'transform: rotate(180deg)')]/div[contains(@style, 'background-image: url(\"/static/media/icon-arrow-left-red.svg\")')]/..")
                    # next_page = driver.find_element(By.XPATH, "//div[contains(@style, 'transform: rotate(180deg)')]/div[contains(@style, '/static/media/icon-arrow-left-red.svg')]/..")
                    next_page = driver.find_element(
                        By.XPATH,
                        # "//div[contains(@class, 'css-1dbjc4n')]/div[contains(@style, 'padding: 4px 8px') and contains(text(), "
                        # "//div[contains(@style, 'padding: 0px; margin: 0px')]/p[contains(@style, 'padding: 4px 8px') and contains(text(), "
                        "//div[contains(@style, 'opacity: 1;')]/p[contains(@style, 'padding: 4px 8px') and contains(text(), "
                        + str(page_number + 1)
                        + ")]",
                    )
                    # print("FOUND Next Page!")
                    logging.info("FOUND Next Page!")
                    # next_page = driver.find_element(By.XPATH, "//div[contains(@class, 'css-1dbjc4n')]/div[contains(@style, 'color: rgb(26, 26, 26); font-family: Poppins-Regular; font-size: 16px; padding: 4px 8px;') and contains(., " + str(page_number) + ")]")

                except (NoSuchElementException, TimeoutException):
                    next_page = None
                    # print("Next Page is not found!")
                    logging.info("Next Page is not found!")
                    is_next_page = False

                    # Darurat
                    # while True:
                    #    pass

                if next_page is not None:
                    # print("Current Page:", page_number, "Next Page:", next_page.text)
                    logging.info(
                        f"Current Page: {page_number} Next Page: {next_page.text}"
                    )
                    page_number += 1
                    # print("Go to Next Page ->", page_number)
                    logging.info(f"Go to Next Page -> {page_number}")
                    next_page.click()
                else:
                    is_next_page = False
                    # print("Next Page is not found! Last Page->", page_number)
                    logging.info(f"Next Page is not found! Last Page->{page_number}")

            except (NoSuchElementException, TimeoutException):
                # print("NOT FOUND")
                logging.info("NOT FOUND")
                # is_next_page = False

        driver.quit()

    # print(result)
    return result
