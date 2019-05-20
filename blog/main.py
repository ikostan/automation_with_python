from blog.app import App
MENU_PROMPT = "Enter 'c' to create a blog, " \
              "'l' to list blogs, " \
              "'r' to read one, " \
              "'p' to create a post, " \
              "or 'q' to quit."


def main():
    #  show user available blogs
    blogs = dict()
    app = App()
    app.print_blogs()

    # Let the user make a choice
    selection = input(MENU_PROMPT)

    # Process the choice
    while selection is not 'q':
        if selection == 'c':
            app.ask_create_blog()
        elif selection == 'l':
            app.print_blogs()
        elif selection == 'r':
            app.ask_read_blog()
        elif selection == 'p':
            app.ask_create_post()
        selection = input(MENU_PROMPT)

