from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys

browser = webdriver.Chrome()
actions = ActionChains(browser)
wait = WebDriverWait(browser, 10)
browser.get('http://instagram.com/')
assert 'Instagram' in browser.title
time.sleep(30)

username = 'your_user_name'
password = 'Your_password'


try:
    # Find the username input
    elem = browser.find_element(By.NAME, 'username')
    elem.send_keys(username + Keys.RETURN)

    # Find the password input field and send keys
    elem_password = browser.find_element(By.NAME, 'password')
    elem_password.send_keys(password + Keys.RETURN)

    # Add a delay to allow time for the page to load (you can adjust the sleep time as needed)
    time.sleep(10)     
    print("login successful")

except:
    # If username input was not found, handle the exception
    print("Already loged in.")

url = 'onetap/?next=%2F'

if url in browser.current_url:
    try:
        button_div = browser.find_element(By.CSS_SELECTOR, 'div[role="button"]')

        # Create an ActionChains object
        actions = ActionChains(browser)

        # Move the cursor to the element's location and click on it
        actions.move_to_element(button_div).click().perform()
    except:
        print("no location")
    
try:
    elem = browser.find_element(By.XPATH,'//button[normalize-space()="Not Now"]').click()                       
    time.sleep(3)
except:
    print("..........")
browser.get('http://instagram.com/explore')
time.sleep(4)

print("opening the explore feed")

x = browser.execute_script("return window.innerWidth;")-50
y = 100

elem = browser.execute_script(f"return document.elementFromPoint({x},{y});")
actions.move_to_element(elem).click().perform()
# elem.click()
time.sleep(2)

print("following the users")
number = 1

for x in range(5):
    try:
        # Find and click the element with partial link text 'likes'
        likes_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'likes')
        likes_link.click()
        time.sleep(20)
        
    except:
        print("Element with partial link text 'likes' not found")
        time.sleep(1)

    try:
        # Find and click the element with partial link text 'others'
        others_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'others')
        others_link.click()
        time.sleep(20)
        
    except:
        print("Element with partial link text 'others' not found")
        time.sleep(1)
    

    try:
            
        elems = browser.find_elements(By.XPATH, "//button[normalize-space()='Follow']")

        if len(elems) > 0:
            elems = elems[1:3]

        for elem in elems:
            actions.move_to_element(elem).perform()
            js_code = "arguments[0].click();"
            browser.execute_script(js_code, elem)
            print('Followed ',number)
            number = number+1
            time.sleep(5)

        time.sleep(1)
            
    except:
        print("page loading error occured ")
        
    try:
        elem = browser.find_element(By.XPATH, "//button[normalize-space()='Close']")
        elem.click()
        time.sleep(1)
        
    except:
        print("skip close")
        
    try:
        elem = browser.find_element(By.XPATH, "//button[normalize-space()='Next']")
        elem.click()
        time.sleep(5)
    except:
        print("skip next")
       