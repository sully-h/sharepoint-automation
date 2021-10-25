import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from info import target_site, chrome_driver_webpath, username, password

driver = webdriver.Chrome(chrome_driver_webpath)

class FormFill:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_webpath)

        self.log_on()

    def log_on(self):

        time.sleep(5)
        self.driver.get(target_site)
        time.sleep(2)

        actions = ActionChains(driver)
        actions.send_keys(username)
        actions.perform()

        for _ in range(3):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()

        actions=actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(2)
        actions.send_keys(password)
        actions.perform()
        for _ in range(2):
            actions=actions.send_keys(Keys.TAB)
        actions.perform()
        actions=actions.send_keys(Keys.ENTER)
        actions.perform()
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    form_filler = FormFill()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
