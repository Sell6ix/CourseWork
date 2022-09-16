import json


def get_all_posts():
    """Возвращает посты"""

    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""

    data = get_all_posts()
    authors = [post['poster_name'] for post in data]
    posts = []
    try:
        if user_name in authors:
            for post in data:
                if user_name == post['poster_name']:
                    posts.append(post)
        else:
            raise ValueError
    except ValueError:
        return f'<h1>Пользователь {user_name} не найден</h1>'
    else:
        return posts


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    new_query=query.lower()
    list_posts = get_all_posts()
    posts = []
    for post in list_posts:
        if new_query in post['content'].lower().strip():
            posts.append(post)
    return posts


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    list_posts = get_all_posts()
    for post in list_posts:
        if pk == post['pk']:
            return post
