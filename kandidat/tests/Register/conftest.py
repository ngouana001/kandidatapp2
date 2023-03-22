import pytest



@pytest.fixture
def kandidat_data():
	return {'email': 'kandidat_email', 'Nachname': 'kandidat_nachname',
	       'Vorname': 'kandiat_vorname', 'geschlecht' : 'kandidat_geschlecht',
	       'Nummer' : 'kandidat_nummer', 'Beschreibung':'kandidat_beschreibung',
	       'username' : 'kandidat_username' , 'password': 'kandidat_password'}


@pytest.fixture
def user_data(kandidat_data):
    return {"username": kandidat_data.get('username'),
            "password": kandidat_data.get('password')}