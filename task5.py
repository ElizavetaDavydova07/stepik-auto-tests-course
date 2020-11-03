from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(a):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    wait_for_text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_tag_name("button")
    button.click()
    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    x_element = browser.find_element_by_css_selector("label :nth-child(2)")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()
finally:
    time.sleep(20)
    browser.quit()
