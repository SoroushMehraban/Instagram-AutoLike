import sys
from time import sleep

from selenium import webdriver


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('chromedriver')
        self.username = username
        self.password = password

        self.driver.get("https://instagram.com")  # opening instagram
        sleep(2)
        self._login(self.username, self.password)
        sleep(6)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self._like()

    def _login(self, username, password):
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)  # entering username
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)  # entering password
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

    def _like(self):
        scroll_counter = SCROLL_TIMES

        while True:
            elements = self.driver.find_elements_by_xpath(
                "//*[name()='svg'][@aria-label='Like']//ancestor::button[@class "
                "='wpO6b ']")  # finding like elements for posts(not for comments)
            for element in elements:  # like each post
                try:
                    element.click()
                except Exception:
                    pass
                sleep(2)

            if scroll_counter == 0:
                scroll_counter = SCROLL_TIMES
                self.driver.refresh()
            else:
                self.driver.execute_script("""
                window.scrollBy(0, 1000);
                """)
                scroll_counter -= 1
            sleep(5)


if __name__ == '__main__':
    SCROLL_TIMES = 100
    my_bot = InstaBot(sys.argv[1], sys.argv[2])
