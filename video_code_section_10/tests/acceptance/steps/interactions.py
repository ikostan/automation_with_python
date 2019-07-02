from behave import *
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage


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
