from behave import *
from selenium import webdriver
from video_code_section_10.tests.acceptance.config import home_url, web_driver_path

use_step_matcher('re')


@given('I am on the home page')
def step_impl(context):

    context.browser = webdriver.Chrome(web_driver_path)
    context.browser.get(home_url)


@given('I am on the blog page')
def step_impl(context):

    context.browser = webdriver.Chrome(web_driver_path)
    context.browser.get(home_url + '/blog')


@then('I am on the blog page')
def step_impl(context):

    expected_url = home_url + '/blog'
    assert context.browser.current_url == expected_url


@then('I am on the home page')
def step_impl(context):

    expected_url = home_url + '/'
    assert context.browser.current_url == expected_url
