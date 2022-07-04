from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.conf import settings


#def get_quota(username='budithegreat09@gmail.com', password='Failover6!'):
def get_quota(username, password):

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
