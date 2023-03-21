from django import urls
from kandidat.models import Kandidat
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param', [
    ('register'),
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    print(temp_url)
    resp = client.get(temp_url)
    assert resp.status_code == 302 or resp.status_code == 200

    @pytest.mark.django_db
    def test_kandidat_register(client, kandidat_data):
        user_data = {"username": kandidat_data.get('username'),
                     "password": kandidat_data.get('password'), 'confirm': kandidat_data.get('password')}

        user_model = get_user_model()
        assert user_model.objects.count() == 0
        register_url = urls.reverse('register')
        resp = client.post(register_url, user_data)
        assert user_model.objects.count() == 1
        assert resp.status_code == 302