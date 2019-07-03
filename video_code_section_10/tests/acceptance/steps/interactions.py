from behave import *
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage
from video_code_section_10.tests.acceptance.page_model.post_page import NewPostPage


use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    
    # in this case link_id = "blog-link" or "home-link"
    # link = context.driver.find_element_by_id(link_text)

    page = BasePage(context.driver)
    links = page.navigation
    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError('No matching nav-links found')


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@step('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.create_button.click()
