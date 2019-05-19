from blog.blog import Blog


class App:
    PROMPT_FOR_BLOG_TITLE = 'Enter your blog title: '
    PROMPT_FOR_AUTHOR_NAME = 'Enter your name: '
    PROMPT_FOR_BLOG_TO_READ = 'Enter your blog title you would like to read: '
    POST_TEMPLATE = '''
                    --- {0} ---
        
                    {1}
                
                    '''

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

    def ask_create_blog(self):
        title = input(self.PROMPT_FOR_BLOG_TITLE)
        author = input(self.PROMPT_FOR_AUTHOR_NAME)
        self.blogs[title] = Blog(title, author)

    def ask_read_blog(self):
        title = input(self.PROMPT_FOR_BLOG_TO_READ)
        self.print_posts(self.blogs[title])

    def print_posts(self, blog):
        for post in blog.posts:
            self.print_post(post)

    def print_post(self, post):
        print(self.POST_TEMPLATE.format(post.title, post.content))

    def ask_create_post(self):
        pass

