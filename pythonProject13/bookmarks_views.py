import logging

from flask import Blueprint, render_template, redirect

from pythonProject13.bookmarks_utils import get_all_bookmarks, add_to_bookmarks, remove_from_bookmarks
from pythonProject13.posts_views import api_logger

boookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')

api_logger = logging.getLogger('api_logger')
api_logger.setLevel(level=logging.INFO)

file_handler = logging.FileHandler("log/api.log", encoding='utf-8')

api_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(api_formatter)

api_logger.addHandler(file_handler)

@boookmarks_blueprint.route("/bookmarks/")
def bookmarks_page():
    api_logger.info('Запрос /api/bookmarks/')
    bookmarks = get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@boookmarks_blueprint.route("/bookmarks/add/<int:post_id>")
def add_to_bookmarks_page(post_id):
    api_logger.info(f'Запрос /api/bookmarks/add/{post_id}')
    add_to_bookmarks(post_id)
    return redirect("/", code=302)


@boookmarks_blueprint.route("/bookmarks/remove/<int:post_id>")
def remove_from_bookmarks_page(post_id):
    api_logger.info(f'Запрос /api/bookmarks/remove/{post_id}')
    remove_from_bookmarks(post_id)
    return redirect("/", code=302)
