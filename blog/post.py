class Post:
    def __init__(self, title: str, content: str):
        self.title = title.capitalize()
        self.content = content

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

