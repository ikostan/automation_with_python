class Post:
    def __init__(self, title: str, content: str):
        # Post Tile (capitalized)
        self.title = title.capitalize()

        # Post Content
        self.content = content

    # JSON
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

