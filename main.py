import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from info import target_site, chrome_driver_webpath, username, password, dates, name, first_name, \
    surname, CID, pay, approver_name


class FormFiller():
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome(chrome_driver_webpath)
        self.driver.get(target_site)
        self.actions = ActionChains(self.driver)

        if kwargs.get("log_on"):
            self.log_on()

    def log_on(self):

        time.sleep(1)

        self.actions.send_keys(username)
        self.actions.perform()
        # Type the username and press Enter
        for _ in range(3):
            self.actions = self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions = self.actions.send_keys(Keys.ENTER)
        self.actions.perform()

        time.sleep(2)
        # Type the password and press Enter
        self.actions.send_keys(password)
        self.actions.perform()

        for _ in range(2):
            self.actions = self.actions.send_keys(Keys.TAB)
        self.actions.perform()
        self.actions = self.actions.send_keys(Keys.ENTER)
        self.actions.perform()

    def fill_form(self, entered_date, hours, holiday, tier_4=None):
        """this method will wait for the first checkbox to appear in HTML then fill in the form according to the data
        desired """
        self.driver.get(target_site)

        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="ctl00_ctl40_g_d9e61186_df86_4651_9116_0d022315872f_FormControl0_V1_I1_C10"]')))

        self.actions = self.actions.send_keys(entered_date)
        self.actions.perform()

        for _ in range(2):
            self.actions = self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions = self.actions.send_keys(hours.get("Monday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(hours.get("Tuesday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(hours.get("Wednesday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()
        self.actions.send_keys(hours.get("Thursday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(hours.get("Friday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(hours.get("Saturday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()
        self.actions.send_keys(hours.get("Sunday"))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        if holiday:
            holiday_radio_button = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_ctl40_g_d9e61186_df86_4651_9116_0d022315872f_FormControl0_V1_I1_C10"]')
            holiday_radio_button.click()
        time.sleep(1)

        for _ in range(2):
            self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(sum(hours.values()))
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(name)
        self.actions.perform()

        time.sleep(3)

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        time.sleep(3)

        for _ in range(4):
            self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(surname)
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(first_name)
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(CID)
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        # unchecks the box if user doesn't use a tier4 visa
        if not tier_4:
            tier_4_radio_button = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_ctl40_g_d9e61186_df86_4651_9116_0d022315872f_FormControl0_V1_I1_C16"]')
            tier_4_radio_button.click()

        self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(pay)
        self.actions.perform()

        time.sleep(2)

        for _ in range(6):
            self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        self.actions.send_keys(approver_name)
        self.actions.perform()

        self.actions.send_keys(Keys.TAB)
        time.sleep(3)

        for _ in range(6):
            self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        time.sleep(2)

        # automatically selects desired value in dropdown options

        self.actions.send_keys("s")
        self.actions.perform()

        for _ in range(2):
            self.actions.send_keys(Keys.TAB)
        self.actions.perform()

        # all that's left now is to click Enter to submit. This is left for the user to do manually after approving
        # the data.


if __name__ == '__main__':
    form_filler = FormFiller(log_on=True)
    for date in dates:
        form_filler.fill_form(date, hours={"Monday": 3, "Tuesday": 4, "Wednesday": 4, "Thursday": 4, "Friday": 3},
                              holiday=True, tier_4=False)

