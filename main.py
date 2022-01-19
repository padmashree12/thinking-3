# import selenium and initialize the webdriver
from selenium import webdriver
import time
from minutemail import Mail
from bs4 import BeautifulSoup
import random
import string
import os

options = webdriver.ChromeOptions()

# add headless option
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


def main():
    mail = Mail()
    # initialize the webdriver
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get("https://passport.forem.com/users/sign_up")
    # find email input
    driver.find_element_by_id("user_email").send_keys(str(mail))
    time.sleep(1)
    # find password input
    driver.find_element_by_id("user_password").send_keys("123456")
    time.sleep(1)
    # find password confirmation input
    driver.find_element_by_id("user_password_confirmation").send_keys("123456")
    time.sleep(2)
    # find submit button
    driver.find_element_by_xpath("//input[@value='Sign up']").click()
    time.sleep(4)
    i = 0
    while True:
        if mail.new_message():  # Check for new mail
            emails = mail.fetch_message()  # Fetch all the messages
            print(emails)
            if len(emails) > 0:
                html = emails[0]['bodyHtmlContent']
                # get the url from the email
                soup = BeautifulSoup(html, 'html.parser')
                url = soup.find('a')['href']
                if len(url) > 0:
                    driver.get(url)
                    time.sleep(2)
                    print(url)
                    break

        time.sleep(6)
        i += 2
        if i > 120:
            driver.quit()
            return

    time.sleep(4)
    # find the terms of service checkbox
    driver.find_element_by_xpath(
        "//input[@id='_user_checked_terms_and_conditions']").click()

    time.sleep(2)
    # find the Next button
    driver.find_element_by_xpath("//input[@value='Next']").click()

    # add implicit wait
    driver.implicitly_wait(10)
    time.sleep(2)
    # find the first name input
    driver.find_element_by_id("_user_name").send_keys("dfgdgfdg")
    time.sleep(3)
    # find the username input
    driver.find_element_by_id("_user_username").send_keys(
        random_string_generator(6, string.ascii_lowercase)
    )
    time.sleep(3)
    # find the file upload button
    driver.find_element_by_xpath(
        "//input[@id='_user_profile_image']").send_keys(
        os.path.join(os.getcwd(), 'elon.png'))

    time.sleep(3)

    # find the Next button
    driver.find_element_by_xpath("//input[@value='Next']").click()
    print("Created profile")
    time.sleep(5)

    # go to dev.to signup page
    driver.get("https://dev.to/enter?state=new-user")
    time.sleep(2)
    # click on `Sign up with Forem` button
    driver.find_element_by_xpath(
        "//button[@class='crayons-btn crayons-btn--l crayons-btn--brand-forem crayons-btn--icon-left grow-1 whitespace-nowrap']").click()
    driver.implicitly_wait(10)
    time.sleep(4)

    # find the `Authorize` button
    driver.find_element_by_xpath("//input[@value='Authorize']").click()
    time.sleep(6)
    print("Signed in to dev.to")
    # find the accept code of conduct checkbox
    driver.find_element_by_xpath(
        "//input[@id='checked_code_of_conduct']").click()

    # find the Terms of Service checkbox
    driver.find_element_by_xpath(
        "//input[@id='checked_terms_and_conditions']").click()

    # find the Continue button
    driver.find_element_by_xpath("//button[@class='next-button']").click()
    time.sleep(2)

    # find the skip-for-now button
    driver.find_element_by_xpath(
        "//button[@class='next-button skip-for-now']").click()
    time.sleep(2)

    # find the Continue button
    driver.find_element_by_xpath("//button[@class='next-button']").click()
    driver.implicitly_wait(10)
    time.sleep(2)

    # find the skip-for-now button
    driver.find_element_by_xpath(
        "//button[@class='next-button skip-for-now']").click()
    time.sleep(2)

    # find the Continue button
    driver.find_element_by_xpath("//button[@class='next-button']").click()
    print("Now I will go to your blog")
    driver.implicitly_wait(10)
    time.sleep(5)

    driver.get("https://dev.to/codewithpom/dev-book-store-c6l")
    time.sleep(2)
    try:
        # find the like button
        driver.find_element_by_xpath(
            "//button[@id='reaction-butt-like']").click()
        time.sleep(1)
    except Exception:
        driver.quit()
        return
    # find the unicorn button
    driver.find_element_by_xpath(
        "//button[@id='reaction-butt-unicorn']").click()
    time.sleep(1)
    # find the bookmark button
    driver.find_element_by_xpath(
        "//button[@id='reaction-butt-readinglist']").click()
    time.sleep(1)
    print("Now Going to second blog")
    driver.get("https://dev.to/codewithpom/c-cheat-sheet-1-4n6n")
    time.sleep(2)
    try:
        # find the like button
        driver.find_element_by_xpath(
            "//button[@id='reaction-butt-like']").click()
        time.sleep(1)
    except Exception:
        driver.quit()
        return
    # find the unicorn button
    driver.find_element_by_xpath(
        "//button[@id='reaction-butt-unicorn']").click()
    time.sleep(1)
    # find the bookmark button
    driver.find_element_by_xpath(
        "//button[@id='reaction-butt-readinglist']").click()
    time.sleep(1)
    # find the follow button
    driver.find_element_by_xpath(
        '//*[@id="article-show-primary-sticky-nav"]/div[1]/div[2]/button').click()

    time.sleep(2)
    print("DONE")
    driver.quit()
# main()


while True:
    try:
        main()
    except Exception as e:
        print(e)
        print("Error")
        continue
