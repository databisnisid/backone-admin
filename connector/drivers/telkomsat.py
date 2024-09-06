from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.conf import settings
from connector.drivers import pop3
from connector.drivers.selenium_utils import find_element_presence, find_element_clickable
from time import sleep


def check_for_error(driver: webdriver.Firefox) -> str:

    delay = 1
    error_msg = ""

    # First Pop Up - Oops!
    try:
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Oops!')]"))
        )

        print("Found Oops!")

        # Get OK Button
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//button/span[contains(text(), 'OK')]"))
        )

        print("Click OK for Oops!")
        elem.click()

    except:
        pass

    driver.implicitly_wait(1)

    # Second Pop Up

    try:
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='/images/icons/ico_error.png']"))
        )
        #elem = WebDriverWait(driver, delay).until(
        #    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Error')]"))
        #)

        elem = driver.find_elements(By.XPATH, "//span")

        print("Error:", elem[1].text)
        error_msg = elem[1].text

        # Get OK Button
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//button/span[contains(text(), 'OK')]"))
        )
        print("Click OK")
        elem.click()

    except:
        pass


    return error_msg


def wait_for_loader(driver: webdriver.Firefox):
    try:
        WebDriverWait(driver, 30).until(
                EC.invisibility_of_element_located((By.XPATH, "//img[@src='/images/loader.gif']"))
        )
    except TimeoutException:
        driver.quit()


def get_quota_value(driver: webdriver.Firefox) -> str:

    elem = find_element_presence(driver, 
    #                             "//div[@class='MyProfilePackageQuotaCard-component__value___bBAlb']",
                                 "//span[text()='MB' or text()='GB' or text()='KB']/..",
                                 30, False)
    quota_value = ""
    if elem:
        quota_value = elem.text
        print("Quota Value: ",quota_value)

    return quota_value


def get_quota_date(driver: webdriver.Firefox) -> str:

    elem = find_element_presence(driver, 
    #                             "//div[@class='MyProfilePackageQuotaCard-component__date___y8Nm3']",
                                 "//span[text()='Until']/..",
                                 30, False)

    quota_date = ""
    if elem:
        quota_date = elem.text
        print("Quota Date:", quota_date)

    return quota_date


def search_by_msisdn(driver: webdriver.Firefox, msisdns: list = []) -> dict:

    if not len(msisdns):
        return {}

    delay: int = 30
    error_msg: str = ""

    result = {}

    for msisdn in msisdns:

        """ input mobileNumber """
        elem = find_element_presence(driver,
                                     "//input[@name='mobileNumber']",
                                     delay, True)
        if elem:
            elem.clear()
            elem.send_keys(msisdn)
            elem.send_keys(Keys.RETURN)
            print("Input MSISDN:", msisdn)

        wait_for_loader(driver)
        error_msg = check_for_error(driver)

        quota_value = ""
        quota_date = ""

        if error_msg == "":

            """ get Quota Info """
            quota_value = get_quota_value(driver)

            """ get Quota Date """
            quota_date = get_quota_date(driver)


        msisdn_result = {
                msisdn : {
                    'quota_value': quota_value,
                    'quota_date': quota_date,
                    'error_msg': error_msg
                    }
                }
        result.update(msisdn_result)


    print('Search By MSISDN is done')
    return result


def login_to_telkomsat(username: str = settings.TELKOMSAT_USERNAME, password: str = settings.TELKOMSAT_PASSWORD) -> dict:

    if username is not None and password is not None:

        print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        if settings.REMOTE_SELENIUM:
            driver_options = webdriver.FirefoxOptions()

            driver = webdriver.Remote(
                command_executor=settings.SELENIUM_DOCKER,
                options=driver_options
            )
        else:
            driver = webdriver.Firefox()

        driver.get(settings.TELKOMSAT_URL)
        delay = 30


        """ Sending Username """
        elem = find_element_presence(driver, 
                                     "//input[@name='username']",
                                     delay, True)
        if elem:
            elem.send_keys(username)
            #elem.send_keys(Keys.RETURN)

        """ Sending Password """
        elem = find_element_presence(driver, 
                                     "//input[@name='password']",
                                     delay, True)
        if elem:
            elem.send_keys(password)
            #elem.send_keys(Keys.RETURN)

        """ Click Button """
        elem = find_element_clickable(driver, 
                                     "//button[@type='submit']",
                                     delay, True)
        if elem:
            elem.click()
            #elem.send_keys(Keys.RETURN)

        

        """ NODELINK """
        """ GET NODELINK PLACEHOLDER """
        sleep(3)
        elem = find_element_presence(driver,
                                      "//div/div/h3[text()='NODELINK']/../..",
                                      delay, True)
        #print(elem.text)
        elem_tbody = elem.find_element(By.TAG_NAME, "tbody")
        elems_tr = elem_tbody.find_elements(By.TAG_NAME, "tr")
        #elem_tbody = elem.find_element(By.XPATH, "//tbody/")
        #elems_tr = elem_tbody.find_elements(By.XPATH, "//tr[@data-state='false']")

        num_elems_tr = len(elems_tr)
        elems_counter = 0

        print("Total Element <tr>:", num_elems_tr)

        while elems_counter < num_elems_tr:
            print("Element Counter:", elems_counter)
            #print(elems_tr[elems_counter].get_attribute('outerHTML'))
            elems_td = elems_tr[elems_counter].find_elements(By.TAG_NAME, "td")
            elems_event = elems_td[0].find_elements(By.TAG_NAME, "div")

            print(elems_td[0].text, elems_td[1].text, elems_td[2].text, elems_td[3].text)
            elems_event[0].click()
            sleep(3)
            driver.back()

            if elems_counter + 1 == num_elems_tr:
                break

            sleep(3)
            elem = find_element_presence(driver,
                                      "//div/div/h3[text()='NODELINK']/../..",
                                      delay, True)

            elem_tbody = elem.find_element(By.TAG_NAME, "tbody")
            elems_tr = elem_tbody.find_elements(By.TAG_NAME, "tr")

            elems_counter += 1

        
        print("Done 1st Page")
        sleep(3)

        try:
            elem = find_element_presence(driver,
                                      "//path[@d='M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z']/../..",
                                      delay, True)

            print(elem)
            elem.click()

        except (NoSuchElementException, TimeoutException):
            pass

        



        driver.quit()

    return result
