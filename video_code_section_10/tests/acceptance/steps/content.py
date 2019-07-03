from behave import *
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage
from video_code_section_10.tests.acceptance.page_model.blog_page import BlogPage


use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):

    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The title has content "(.*)"')
def step_impl(context, content):

    page = BasePage(context.driver)
    assert page.title.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):

    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):

    page = BlogPage(context.driver)
    post_with_title = [post for post in page.posts if post.text == title]

    if len(post_with_title) == 0:
        raise RuntimeError('There is no such post {0}'.format(title))
    else:
        assert all([post.is_displayed() for post in post_with_title if post.text == title])

