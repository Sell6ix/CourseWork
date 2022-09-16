from pythonProject13.utils import get_all_posts

posts_keys = [key for key in get_all_posts()[0].keys()]


class TestApi:

    def test_api(self, test_client):
        response = test_client.get('/api/posts/', follow_redirects=True)
        assert type(response.json) == list, "Статус-код всех постов неверный"
        assert set(response.json[0].keys()) == set(posts_keys), "неверный список ключей"

    def test_api_post(self, test_client):
        response = test_client.get('/api/posts/2', follow_redirects=True)
        assert type(response.json) == dict, "Статус-код всех постов неверный"
        assert set(response.json.keys()) == set(posts_keys), "неверный список ключей"