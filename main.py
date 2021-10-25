import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from info import target_site, chrome_driver_webpath, username, password, dates, practice_dates, name, first_name, surname, CID, pay, approver_name

driver = webdriver.Chrome(chrome_driver_webpath)


def print_hi():
    # Use a breakpoint in the code line below to debug your script.

    driver.get(target_site)
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(username)
    actions.perform()

    # TODO submit username
    # TODO press Tab 3x
    for _ in range(3):
        actions = actions.send_keys(Keys.TAB)
    actions.perform()
    # TODO press Enter
    actions = actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(2)
    # TODO enter pw
    actions.send_keys(password)
    actions.perform()



    # TODO enter Tab twice and enter the password
    for _ in range(2):
        actions = actions.send_keys(Keys.TAB)
    actions.perform()
    actions = actions.send_keys(Keys.ENTER)
    actions.perform()

    wait = WebDriverWait(driver, 100)
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="ctl00_ctl40_g_d9e61186_df86_4651_9116_0d022315872f_FormControl0_V1_I1_C10"]')))

    # # TODO Press Enter to stay signed in
    # actions = actions.send_keys(Keys.ENTER)
    # actions.perform()

    #TODO paste in details
    for date in practice_dates:
        actions = actions.send_keys(date)
        actions.perform()

        for _ in range(2):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()

        actions=actions.send_keys(3)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(4)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(4)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()
        actions.send_keys(4)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(3)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(0)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()
        actions.send_keys(0)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        holiday_radio_button= driver.find_element_by_xpath('//*[@id="ctl00_ctl40_g_d9e61186_df86_4651_9116_0d022315872f_FormControl0_V1_I1_C10"]')
        holiday_radio_button.click()
        time.sleep(1)
        #now for total hours per week

        for _ in range(2):
            actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(18)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(name)
        actions.perform()

        time.sleep(3)

        actions.send_keys(Keys.TAB)
        actions.perform()

        time.sleep(3)


        for _ in range(4):
            actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(surname)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(first_name)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(CID)
        actions.perform()

        actions.send_keys(Keys.TAB)
        actions.perform()

        tier_4_radio_button= driver.find_element_by_xpath('//*[@id="ctl00_ctl40_g_d9e61186_df86_4651_9116_0d022315872f_FormControl0_V1_I1_C16"]')
        tier_4_radio_button.click()

        actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(pay)
        actions.perform()

        time.sleep(2)

        for _ in range(6):
            actions.send_keys(Keys.TAB)
        actions.perform()

        actions.send_keys(approver_name)
        actions.perform()

        actions.send_keys(Keys.TAB)
        time.sleep(3)

        for _ in range(6):
            actions.send_keys(Keys.TAB)
        actions.perform()

        time.sleep(2)

        actions.send_keys("s")
        actions.perform()

        for _ in range(2):
            actions.send_keys(Keys.TAB)
        actions.perform()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
