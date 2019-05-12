from blog.blog import Blog


class App:
    def __init__(self):
        # Mapping of blog_name: blog object
        self.blogs = dict()

    def menu(self):
        # Show the user available blogs
        # Let the user make a choice
        # Process the choice
        # Eventually exit
        pass

    def add_blog(self, blog_name: str, blog: Blog):
        blog_name = ' '.join([item.capitalize() for item in blog_name.split(' ')])
        self.blogs.update({blog_name: blog})

    def print_blogs(self):
        # Print the available blogs
        # Key - blog name, value - Blog
        for key, value in self.blogs.items():
            print("- {0}".format(value))


