from behave import *
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage


use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    # title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    # assert title_tag.is_displayed()
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The title has content "(.*)"')
def step_impl(context, content):
    # title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    # assert title_tag.text == content
    page = BasePage(context.driver)
    assert page.title.text == content

