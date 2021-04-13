from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://output.jsbin.com/radara')


try:
    email = driver.find_element_by_css_selector('#email')
    if email != None:
        print('TEST PASS: Email exists')
except Exception as e:
    print('TEST FAIL: Email not found')

try:
    password = driver.find_element_by_css_selector('#password')
    if password != None:
        print('TEST PASS: Password exists')
except Exception as e:
    print('TEST FAIL: Password not found')

try:
    submit = driver.find_element_by_css_selector('#login')
    if password != None:
        print('TEST PASS: Submit button exists')
except Exception as e:
    print('TEST FAIL: Submit button not found')

try:
    asdf = driver.find_element_by_css_selector('#asdf')
    if asdf != None:
        print('TEST PASS: How?')
except Exception as e:
    print('TEST FAIL: Asdf not found')

driver.quit()
