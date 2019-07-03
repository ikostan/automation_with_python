from video_code_section_10.tests.acceptance.locators.new_post_page import NewPostPageLocator
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage
from selenium.webdriver.common.by import By


class NewPostPage(BasePage):

    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocator.NEW_POST_FORM)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

    @property
    def blog_link(self):
        return self.driver.find_element(*NewPostPageLocator.NAVIGATION_LINK)

    @property
    def create_button(self):
        return self.driver.find_element(*NewPostPageLocator.CREATE_BUTTON)

    '''
    @property
    def title_field(self):
        return self.driver.find_element(*NewPostPageLocator.TITLE_FIELD)

    @property
    def content_field(self):
        return self.driver.find_element(*NewPostPageLocator.CONTENT_FIELD)
    '''
