from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the home page')
def step_impl(context):
    path = 'C:/Users/superadmin/Desktop/Python/automation_with_python/' \
           'video_code_section_10/webdriver/win32/74.0.3729.6/chromedriver.exe'
    browser = webdriver.Chrome(path)
    browser.get('http://127.0.0.1:5000')
