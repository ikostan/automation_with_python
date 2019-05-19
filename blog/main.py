from blog.app import App
from blog.blog import Blog


def main():
    #  show user available blogs
    blogs = dict()
    app = App()
    app.print_blogs()
    app.menu()

