
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

    def print_blogs(self):
        # Print the available blogs
        # Key - blog name, value - Blog
        for key, value in self.blogs.items():
            print("- {0}".format(value))


