from video_code_section_10.tests.acceptance.locators.post_page import PostPageLocator
from video_code_section_10.tests.acceptance.page_model.base_page import BasePage


class PostPage(BasePage):

    @property
    def url(self):
        return super(PostPage, self).url + '/post'

    @property
    def blog_link(self):
        return self.driver.find_element(*PostPageLocator.NAVIGATION_LINK)
