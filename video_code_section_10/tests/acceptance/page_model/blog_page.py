from video_code_section_10.tests.acceptance.locators.blog_page import BlogPageLocator
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):

    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocator.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_element(*BlogPageLocator.POST)

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocator.ADD_POST_LINK)

    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocator.NAVIGATION_LINK)
