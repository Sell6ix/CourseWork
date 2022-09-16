from flask import Flask

from pythonProject13.bookmarks_views import boookmarks_blueprint
from pythonProject13.posts_views import posts_blueprint

app = Flask(__name__)



app.register_blueprint(posts_blueprint)
app.register_blueprint(boookmarks_blueprint)


if __name__ == "__main__":
    app.run()
