from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: pressence_of_element_located(By.XPATH, ".//*[@id='button-1005']"))
        driver.find_element_by_xpath(self.locator).click()
