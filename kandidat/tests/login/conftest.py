import pytest
from kandidat.models import Kandidat
from django.contrib.auth import get_user_model


@pytest.fixture
def kandidat_data():
    return {'email': 'kandidat_email', 'Nachname': 'kandidat_nachname',
            'Vorname': 'kandiat_vorname', 'geschlecht': 'kandidat_geschlecht',
            'Nummer': 'kandidat_nummer', 'Beschreibung': 'kandidat_beschreibung',
            'username': 'kandidat_username', 'password': 'kandidat_password'}
@pytest.fixture
def user_data(kandidat_data):
    return {"username": kandidat_data.get('username'),
            "password": kandidat_data.get('password')}
@pytest.fixture
def create_test_kandidat(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user


@pytest.fixture
def authenticated_kandidat(client, user_data):
    user_model = get_user_model()

    test_kandidat = user_model.objects.create_user(**user_data)
    test_kandidat.save()
    client.login(**user_data)
    return test_kandidat