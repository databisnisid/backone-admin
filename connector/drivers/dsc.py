from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.conf import settings
from connector.drivers import pop3
from connector.drivers.selenium_utils import (
    find_element_presence,
    find_element_clickable,
)
from time import sleep
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# def check_for_error(driver: webdriver.Firefox, delay: int = 5) -> str:
def check_for_error(driver, delay: int = 5) -> str:

    error_msg = ""

    # First Pop Up - Oops!
    try:
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Oops!')]")
            )
        )

        # print("Found Oops!")
        logging.info("Found Oops!")

        # Get OK Button
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button/span[contains(text(), 'OK')]")
            )
        )

        # print("Click OK for Oops!")
        logging.info("Click OK for Oops!")
        elem.click()

    except:
        pass

    driver.implicitly_wait(delay)

    # Second Pop Up

    try:
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@src='/images/icons/ico_error.png']")
            )
        )
        # elem = WebDriverWait(driver, delay).until(
        #    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Error')]"))
        # )

        elem = driver.find_elements(By.XPATH, "//span")

        # print("Error:", elem[1].text)
        logging.info(f"Error: {elem[1].text}")
        error_msg = elem[1].text

        # Get OK Button
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button/span[contains(text(), 'OK')]")
            )
        )
        # print("Click OK")
        logging.info("Click OK")
        elem.click()

    except:
        pass

    # return error_msg
    return error_msg[:200]


# def wait_for_loader(driver: webdriver.Firefox, delay: int = 300):
def wait_for_loader(driver, delay: int = 300):

    logging.info("Waiting for loader...")

    try:
        WebDriverWait(driver, delay).until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//img[@src='/images/loader.gif']")
            )
        )
    except TimeoutException:
        driver.quit()


# def get_quota_value(driver: webdriver.Firefox, delay: int = 300) -> str:
def get_quota_value(driver, delay: int = 300) -> str:

    elem = find_element_presence(
        driver,
        #                             "//div[@class='MyProfilePackageQuotaCard-component__value___bBAlb']",
        "//span[text()='MB' or text()='GB' or text()='KB']/..",
        delay,
        False,
    )
    quota_value = ""
    if elem:
        quota_value = elem.text
        print("Quota Value: ", quota_value)

    return quota_value


# def get_quota_date(driver: webdriver.Firefox, delay: int = 300) -> str:
def get_quota_date(driver, delay: int = 300) -> str:

    elem = find_element_presence(
        driver,
        #                             "//div[@class='MyProfilePackageQuotaCard-component__date___y8Nm3']",
        "//span[text()='Until']/..",
        delay,
        False,
    )

    quota_date = ""
    if elem:
        quota_date = elem.text
        # print("Quota Date:", quota_date)
        logging.info(f"Quota Date: {quota_date}")

    return quota_date


# def search_by_msisdn(driver: webdriver.Firefox, msisdns: list = []) -> dict:
def search_by_msisdn(driver, msisdns: list = []) -> dict:

    if not len(msisdns):
        return {}

    delay: int = 60
    error_msg: str = ""

    result = {}

    for msisdn in msisdns:

        """input mobileNumber"""
        elem = find_element_presence(
            driver, "//input[@name='mobileNumber']", delay, True
        )
        if elem:
            elem.clear()
            elem.send_keys(msisdn)
            elem.send_keys(Keys.RETURN)
            # print("Input MSISDN:", msisdn)
            logging.info(f"Input MSISDN: {msisdn}")

        wait_for_loader(driver)
        error_msg = check_for_error(driver)

        quota_value = ""
        quota_date = ""

        if error_msg == "":

            """get Quota Info"""
            quota_value = get_quota_value(driver)

            """ get Quota Date """
            quota_date = get_quota_date(driver)

        msisdn_result = {
            msisdn: {
                "quota_value": quota_value,
                "quota_date": quota_date,
                "error_msg": error_msg,
            }
        }
        result.update(msisdn_result)

    # print("Search By MSISDN is done")
    logging.info("Search By MSISDN is done")
    return result


def login_to_dsc(
    msisdns: list = [],
    username: str = settings.DSC_USERNAME,
    password: str = settings.DSC_PASSWORD,
    email_address: str = settings.DSC_EMAIL_ADDRESS,
    email_password: str = settings.DSC_EMAIL_PASSWORD,
    delay: int = 300,
) -> dict:

    if not len(msisdns):
        return {}

    # Ensure no email
    # print("Delete All Email...")
    logging.info("Delete All Email...")
    pop3.delete_all_email(email_address, email_password)

    # if username is not None and password is not None:
    if username is not None:

        # print("Use Selenium Server: ", settings.REMOTE_SELENIUM)
        logging.info(f"Use Selenium Server: {settings.REMOTE_SELENIUM}")
        if settings.REMOTE_SELENIUM:
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

        driver.get("https://dsc.telkomsel.com")

        """ Sending Username """
        elem = find_element_presence(
            driver, "//input[@name='mobileNumberOrEmail']", delay, True
        )
        if elem:
            elem.send_keys(username)
            elem.send_keys(Keys.RETURN)

        """ Check Term and Condition """
        elem = find_element_clickable(driver, "//input[@id='acceptTnc']", delay, True)
        if elem:
            wait_for_loader(driver)
            elem.click()

        """ Click GET CODE Button """
        elem = find_element_clickable(driver, "//button[@type='button']", delay, True)

        if elem:
            wait_for_loader(driver)
            elem.click()

        """ 
        Function to get Code from email
        Use poplib 
        """
        for i in range(1, 120):
            # print("Trying get code #" + str(i))
            logging.info(f"Trying get code #{str(i)}")
            otp_code = pop3.get_otp_code(email_address, email_password)
            if otp_code != "":
                # print("OTP Code:", otp_code)
                logging.info(f"OTP Code: {otp_code}")
                break
            sleep(3)

        """ Enter CODE """
        elem = find_element_presence(driver, "//input[@name='otp']", delay, True)

        if elem:
            elem.send_keys(otp_code)

        """ SUBMIT """
        elem = find_element_clickable(driver, "//button[@type='submit']", delay, True)
        if elem:
            wait_for_loader(driver)
            elem.click()

        """ myServices """
        elem = find_element_clickable(driver, "//div[@id='myServices']", delay, True)
        if elem:
            wait_for_loader(driver)
            elem.click()
            # print("Click myServices")
            logging.info("Click myServices")

        """ checkmember """
        elem = find_element_clickable(
            driver, "//a[@href='/pic/check-member']", delay, True
        )
        if elem:
            wait_for_loader(driver)
            elem.click()
            # print("Click Check Member")
            logging.info("Click Check Member")

        # msisdns = ['6281117064193', '62811170668622', '6281117064195']
        result = search_by_msisdn(driver, msisdns)

        # print("So Farrr...Quit")
        logging.info("So Farrr...Quit")

        driver.quit()

    return result
