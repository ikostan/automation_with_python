from video_code_section_10.tests.acceptance.locators.base_page import BasePageLocator


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        '''
        Returns root directory/url
        :return:
        '''
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        '''
        Returns page title
        :return:
        '''
        return self.driver.find_element(*BasePageLocator.TITLE)

    @property
    def navigation(self):
        '''
        Returns all navigation links
        :return:
        '''
        return self.driver.find_elements(*BasePageLocator.NAV_LINKS)
