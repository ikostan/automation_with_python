from blog.post import Post


class Blog:
    def __init__(self, title: str, author: str):
        # Blog Title
        self.title = ' '.join(x.capitalize() for x in title.split(' '))

        # Author Name (capitalized)
        self.author = ' '.join(x.capitalize() for x in author.split(' '))

        # All the posts of the related author
        self.posts = []

    def __repr__(self):
        return '{0} by {1} ({2} post{3})'.format(self.title,
                                                 self.author,
                                                 len(self.posts),
                                                 's' if len(self.posts) > 1 else '')

    def create_post(self, title: str, content: str):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }


