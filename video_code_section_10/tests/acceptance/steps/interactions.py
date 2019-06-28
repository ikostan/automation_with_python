from behave import *

use_step_matcher('re')


@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    
    #  in this case link_id = "blog-link" or "home-link"
    link = context.driver.find_element_by_id(link_id)
    link.click()
