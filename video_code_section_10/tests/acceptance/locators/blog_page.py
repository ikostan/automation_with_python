from selenium.webdriver.common.by import By


class BlogPageLocator:
    ADD_POST_LINK = (By.ID, 'add-post-link')
    POSTS_SECTION = (By.ID, 'posts')
    POST = (By.CLASS_NAME, 'post-link')
    NAVIGATION_LINK = (By.ID, 'home-link')
