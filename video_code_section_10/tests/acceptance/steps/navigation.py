from behave import *
from selenium import webdriver
from video_code_section_10.tests.acceptance.config import web_driver_path, home_url
from video_code_section_10.tests.acceptance.page_model.home_page import HomePage
from video_code_section_10.tests.acceptance.page_model.blog_page import BlogPage


use_step_matcher('re')


@given('I am on the "home" page')
def step_impl(context):

    context.driver = webdriver.Chrome(web_driver_path)
    page = HomePage(context.driver.maximize_window())
    context.driver.get(page.url)


@then('I am on the "blog" page')
def step_impl(context):

    expected_url = home_url + '/blog'
    assert context.driver.current_url == expected_url


@given('I am on the "blog" page')
def step_impl(context):

    context.driver = webdriver.Chrome(web_driver_path)
    page = BlogPage(context.driver.maximize_window())
    context.driver.get(page.url)


@then('I am on the "home" page')
def step_impl(context):

    expected_url = home_url + '/'
    assert context.driver.current_url == expected_url
