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
            #options = webdriver.ChromeOptions()
            options = webdriver.FirefoxOptions()
            options.headless = False
            #driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
            #driver = webdriver.Firefox("/usr/local/bin/geckodriver", options=options)
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

        """ Get Quota Multi Information """
        is_next_page = True
        page_number = 1
        while is_next_page:
            try:
                elem = WebDriverWait(driver, delay).until(
                    #EC.presence_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n']//div[contains(@class, 'css-1dbjc4n') and contains(@class, 'r-18u37iz')]"))
                    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '628')]"))
                )
                time.sleep(delay)


                table_elements = driver.find_elements(By.XPATH, "//div[contains(text(), '628')]/..")
                print("FOUND MSISDN!")
                #print(table_elements)
                for element in table_elements:
                    msisdn = element.find_element(By.XPATH, ".//div[contains(text(), '628')]").text
                    print('Found MSISDN: ', msisdn)
                    quota = element.find_element(By.XPATH, ".//div[contains(text(), ' GB')]").text
                    #quota = element.find_element(By.XPATH, ".//div[contains(text(), 'GB')]").text
                    print('Found Quota Info: ', quota)
                    '''
                    try:
                        quota = element.find_element(By.XPATH, ".//div[contains(text(), 'GB')]").text
                        print('Found Quota Info in GB: ', quota)
                        try:
                            quota = element.find_element(By.XPATH, ".//div[contains(text(), 'MB')]").text
                            print('Found Quota Info in MB: ', quota)
                        except (NoSuchElementException, TimeoutException):
                            quota = None

                    except (NoSuchElementException, TimeoutException):
                        quota = None

                    '''

                    try:
                        until = element.find_element(By.XPATH, ".//div[contains(text(), 'Berlaku')]").text.replace('Berlaku hingga ', '')
                        print('Found Masa Belaku Info: ', until)
                    except (NoSuchElementException, TimeoutException):
                        until = None

                    result[msisdn] = [quota] + [until]
                    #print(result[msisdn])

                #page_number += 1
                try:
                    #next_page = driver.find_element(By.XPATH, "//div[contains(@style, 'transform: rotate(180deg)')]/div[contains(@style, 'background-image: url(\"/static/media/icon-arrow-left-red.svg\")')]/..")
                    #next_page = driver.find_element(By.XPATH, "//div[contains(@style, 'transform: rotate(180deg)')]/div[contains(@style, '/static/media/icon-arrow-left-red.svg')]/..")
                    next_page = driver.find_element(By.XPATH, "//div[contains(@class, 'css-1dbjc4n')]/div[contains(@style, 'padding: 4px 8px') and contains(text(), " + str(page_number + 1) + ")]")
                    print("FOUND Next Page!")
                    #next_page = driver.find_element(By.XPATH, "//div[contains(@class, 'css-1dbjc4n')]/div[contains(@style, 'color: rgb(26, 26, 26); font-family: Poppins-Regular; font-size: 16px; padding: 4px 8px;') and contains(., " + str(page_number) + ")]")

                except (NoSuchElementException, TimeoutException):
                    next_page = None
                    print("Next Page is not found!")
                    is_next_page = False

            
                if next_page is not None:
                    print("Current Page:", page_number, "Next Page:", next_page.text)
                    page_number += 1
                    print('Go to Next Page ->', page_number)
                    next_page.click()
                else:
                    is_next_page = False
                    print('Next Page is not found! Last Page->', page_number)

            except (NoSuchElementException, TimeoutException):
                print("NOT FOUND")
                #is_next_page = False

        driver.quit()

    print(result)
    return result
