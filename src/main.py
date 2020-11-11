from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    executable_path='/home/serpant/python/src/chromedriver')

browser.set_window_size(900, 900)

browser.set_window_position(0, 0)
sleep(1)
wait = WebDriverWait(browser, 10)
browser.get('https://make.powerapps.com/')


# The email page
wait.until(EC.presence_of_element_located((By.ID, "i0116")))

email_textbox = browser.find_element_by_id("i0116")

email_textbox.send_keys("sal@hopelink.org")

wait.until(EC.presence_of_element_located((By.ID, "idSIButton9")))

next_button_email = browser.find_element_by_id("idSIButton9")

next_button_email.click()

# wait until the password page
sleep(5)


# The password page
password_textbox = browser.find_element_by_id("i0118")

password_textbox.send_keys("96SmokingDogs#")

sign_in_button = browser.find_element_by_id("idSIButton9")

sign_in_button.click()

# wait until the stay log in page
wait.until(EC.presence_of_element_located((By.ID, "idBtn_Back")))


# The stay log in page
dont_stay_sign_in_button = browser.find_element_by_id("idBtn_Back")

dont_stay_sign_in_button.click()

# wait until the power apps main dashboard page
wait.until(EC.presence_of_element_located((By.ID, "id__22")))

# the main powerapps dashboard page
app_button = browser.find_element_by_id("id__22")

app_button.click()

# wait until the app list
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "CSP Programs Hub")))

# the app list page
browser.find_element_by_link_text("CSP Programs Hub").click()

# wait until the CSP app is loaded
sleep(60)

tt = browser.find_elements_by_css_selector('body')

print(tt)
print(tt[0].get_attribute('class'))
# print(tt[0].get_attribute('innerHTML'))

# tt.click()

# client_button = browser.find_elements_by_css_selector('li')

# print(client_button)

# client_button.click()

# browser.find_element_by_id('sitemap-entity-New_SubArea').click()

# sleep(20)
# browser.quit()
