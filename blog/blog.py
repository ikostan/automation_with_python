class Blog:
    def __init__(self, title: str, author: str):
        # Blog Title
        self.title = title.capitalize()

        # Author Name (capitalized)
        self.author = ' '.join(x.capitalize() for x in author.split(' '))

        # All the posts of the related author
        self.posts = []


