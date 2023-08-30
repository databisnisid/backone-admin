from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def orbit_selenium():
    #driver = webdriver.Firefox()
    #driver_option = webdriver.FirefoxOptions()
    driver_option = webdriver.ChromeOptions()
    #driver_option.add_argument('-profile /home/dsutanto/Selenium/profile.Selenium')
    #driver_option.headless = True
    driver = webdriver.Remote(
        command_executor='http://192.168.192.8:4444',
        options=driver_option
    )
    driver.get("https://www.myorbit.id/en/login")
    delay = 10
    #quota_string = ""
    #max_quota_string = ""
    #day_string =""
    email_address = "budithegreat09@gmail.com"
    password = "Failover6!"
    try:
        elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@label, 'Email Addres/Phone Number')]")))
        elem.send_keys(email_address)
        elem.send_keys(Keys.RETURN)
    except NoSuchElementException:
        driver.quit()

    try:
        elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@label, 'Password')]")))
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
    except NoSuchElementException:
        driver.quit()

    try:
        """ Find Element where the quota and total quota """
        elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "package-meter-chart")))
        quota_string = elem.find_element(By.XPATH, "./div[2]/div[2]/div[1]")
        max_quota_string = elem.find_element(By.XPATH, "./div[2]/div[2]/div[3]")
        elem_orbit = driver.find_element(By.XPATH, "//*[text()='Internet Orbit']/span")

        print(elem_orbit.text)
        print(quota_string.text)
        print(max_quota_string.text)
    except NoSuchElementException:
        pass

    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    orbit_selenium()


