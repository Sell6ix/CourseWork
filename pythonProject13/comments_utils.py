import json


def get_all_comments():
    """Возвращает все комментарии"""

    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def get_all_posts():
    """Возвращает все посты"""

    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())



def get_comments_by_post_id(post_id):
    """Возвращает комментарии к определенному посту"""

    data = get_all_comments()
    posts = get_all_posts()
    post_ids = [post['pk'] for post in posts]
    comments = []
    try:
        if post_id in post_ids:
            for comment in data:
                if post_id == comment['post_id']:
                    comments.append(comment)
        else:
            raise ValueError
    except ValueError:
        return f'<h1>Пост {post_id} не найден</h1>'
    else:
        return comments
