from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from video_code_section_10.tests.acceptance.locators.blog_page import BlogPageLocator


use_step_matcher('re')


@given('I wait for the posts to load')
def stem_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BlogPageLocator.POSTS_SECTION)
    )

