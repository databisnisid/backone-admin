import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.conf import settings


#def get_quota(username='budithegreat09@gmail.com', password='Failover6!'):
def get_quota_multi(username, password):

    quota_current = ''
    quota_total = ''
    quota_day = ''

    result = {}
    if username is not None and password is not None:

        print('Use Selenium Server: ', settings.REMOTE_SELENIUM)
        if settings.REMOTE_SELENIUM:
            driver_options = webdriver.ChromeOptions()
            #driver_options = webdriver.FirefoxOptions()

            driver = webdriver.Remote(
                command_executor=settings.SELENIUM_DOCKER,
                options=driver_options
            )
        else:
            options = webdriver.ChromeOptions()
            options.headless = False
            driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
            #driver = webdriver.Firefox()

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

        """ Get Quota Multi Information """
        is_next_page = True
        while is_next_page:
            try:
                elem = WebDriverWait(driver, delay).until(
                    #EC.presence_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n']//div[contains(@class, 'css-1dbjc4n') and contains(@class, 'r-18u37iz')]"))
                    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '628')]"))
                )
                time.sleep(delay)


                table_elements = driver.find_elements(By.XPATH, "//div[contains(text(), '628')]/..")
                print("FOUND!")
                #print(table_elements)
                for element in table_elements:
                    msisdn = element.find_element(By.XPATH, ".//div[contains(text(), '628')]").text
                    quota = element.find_element(By.XPATH, ".//div[contains(text(), 'GB')]").text

                    try:
                        until = element.find_element(By.XPATH, ".//div[contains(text(), 'Berlaku')]").text.replace('Berlaku hingga ', '')
                    except (NoSuchElementException, TimeoutException):
                        until = None

                    result[msisdn] = [quota] + [until]
                    #print(result[msisdn])

                try:
                    #next_page = driver.find_element(By.XPATH, "//div[contains(@style, 'transform: rotate(180deg)')]/div[contains(@style, 'background-image: url(\"/static/media/icon-arrow-left-red.svg\")')]/..")
                    next_page = driver.find_element(By.XPATH, "//div[contains(@style, 'transform: rotate(180deg)')]/div[contains(@style, '/static/media/icon-arrow-left-red.svg')]/..")

                except (NoSuchElementException, TimeoutException):
                    next_page = None

                if next_page:
                    print('Go to Next Page')
                    next_page.click()
                else:
                    is_next_page = False

            except (NoSuchElementException, TimeoutException):
                print("NOT FOUND")

        driver.quit()

    print(result)
    return result