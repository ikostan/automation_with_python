from blog.blog import Blog
MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit."


class App:
    def __init__(self):
        # Mapping of blog_name: blog object
        self.blogs = dict()

    def add_blog(self, blog_name: str, blog: Blog):
        blog_name = ' '.join([item.capitalize() for item in blog_name.split(' ')])
        self.blogs.update({blog_name: blog})

    def print_blogs(self):
        # Print the available blogs
        # Key - blog name, value - Blog
        for key, value in self.blogs.items():
            print("- {0}".format(value))

    def menu(self):
        # Let the user make a choice
        selection = input(MENU_PROMPT)
        # Process the choice
        # Eventually exit




