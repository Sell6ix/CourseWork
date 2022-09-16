import logging
from flask import Blueprint, request, render_template, jsonify
from pythonProject13.comments_utils import get_comments_by_post_id
from pythonProject13.bookmarks_utils import get_all_bookmarks
from pythonProject13.utils import get_all_posts, get_post_by_pk, get_posts_by_user, search_for_posts

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')


api_logger = logging.getLogger('api_logger')
api_logger.setLevel(level=logging.INFO)

file_handler = logging.FileHandler("log/api.log", encoding='utf-8')

api_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(api_formatter)

api_logger.addHandler(file_handler)


@posts_blueprint.route("/")
def main_page():
    api_logger.info(f'Запрос /api/')
    posts = get_all_posts()
    all_bookmarks = get_all_bookmarks()
    return render_template('index.html', posts=posts, len_bookmarks=len(all_bookmarks))


@posts_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    api_logger.info(f'Запрос /api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, len_comments=len(comments), comments=comments)


@posts_blueprint.route("/users/<username>")
def user_page(username):
    api_logger.info(f'Запрос /api/users/{username}')
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)


@posts_blueprint.route("/search")
def search_page():
    query = request.args.get('s')
    api_logger.info('Запрос /api/search')
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts, len_posts=len(posts))


@posts_blueprint.route("/api/posts/")
def api_posts_page():
    api_logger.info('Запрос /api/posts')
    posts = get_all_posts()
    return jsonify(posts)


@posts_blueprint.route("/api/posts/<int:post_id>/")
def api_post_page(post_id):
    api_logger.info(f'Запрос /api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    return jsonify(post)
