from selenium.webdriver.common.by import By


class NewPostPageLocator:

    NEW_POST_FORM = (By.ID, 'post-form')
    TITLE_FIELD = (By.ID, 'title')
    CONTENT_FIELD = (By.ID, 'content')
    CREATE_BUTTON = (By.ID, 'create-post')
    NAVIGATION_LINK = (By.ID, 'blog-link')
