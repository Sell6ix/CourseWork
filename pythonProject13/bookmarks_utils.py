import json

from pythonProject13.utils import get_all_posts


def get_all_bookmarks():
    """Получает все сохраненные закладки"""

    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def save_to_bookmark(bookmarks):
    """Сохраняет обновленный список закладок"""

    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        return json.dump(bookmarks, file, ensure_ascii=False)


def add_to_bookmarks(post_id):
    """Добавляет пост в закладки"""
    posts = get_all_posts()
    bookmarks = get_all_bookmarks()
    for post in posts:
        if post_id == post['pk']:
            bookmarks.append(post)
    return save_to_bookmark(bookmarks)


def remove_from_bookmarks(post_id):
    """Удаляет пост из закладок"""

    bookmarks = get_all_bookmarks()
    for bookmark in bookmarks:
        if post_id == bookmark['pk']:
            bookmarks.remove(bookmark)
    return save_to_bookmark(bookmarks)
