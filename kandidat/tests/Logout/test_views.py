from django import urls
from kandidat.models import Kandidat
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param', [
    ('kandidat-home'),
    ('register'),
    ('login')

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


@pytest.mark.django_db
def test_kandidat_login(client, create_test_kandidat, kandidat_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data=kandidat_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('kandidat-home')

@pytest.mark.django_db
def test_user_logout(client, authenticated_kandidat):
    logout_url = urls.reverse('logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('login')