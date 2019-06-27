from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/blog')
def blog_page():
    return render_template('blog.html', posts=posts)


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        global posts

        posts.append({
            'title': title,
            'content': content
        })

        return redirect(url_for('blog_page'))
    return render_template('new_post.html')


@app.route('/post/<string:title>')
def see_post(title):
    global posts

    for post in posts:
        if post['title'] == title:
            return render_template('post.html', post=post)

    return render_template('post.html', post=None)


def shutdown_server():
    '''
    The Werkzeug server that is used by the app.run() command
    can be shut down starting with Werkzeug 0.8.
    This can be helpful for small applications that should serve as a
    frontend to a simple library on a user's computer.
    :return:
    '''
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    '''
    You can shutdown the server by calling this function.
    The shutdown functionality is written in a way that the server
    will finish handling the current request and then stop.

    Source: http://flask.pocoo.org/snippets/67/
    :return:
    '''
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(debug=True)
