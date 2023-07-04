from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from kandidat.models import Kandidat
from django.utils import timezone
import json

# Ici, on crée une classe pour les tests qui hérite de TestCase. 
# Cela nous donne accès à beaucoup de méthodes de test utiles.
class KandidatTestCase(TestCase):
    # La méthode setUp est exécutée avant chaque test. 
    # Nous l'utilisons pour créer un client de test et deux objets Kandidat.
    def setUp(self):
        self.client = Client()
        self.kandidat1 = Kandidat.objects.create(
            Vorname="Kandidat1", 
            Nachname="Nachname1", 
            geschlecht="M", 
            email="kandidat1@example.com", 
            Nummer="1234567890", 
            Beschreibung="Test Candidate 1", 
            ist_erwachsene=True
        )
        self.kandidat2 = Kandidat.objects.create(
            Vorname="Kandidat2", 
            Nachname="Nachname2", 
            geschlecht="F", 
            email="kandidat2@example.com", 
            Nummer="0987654321", 
            Beschreibung="Test Candidate 2", 
            ist_erwachsene=False
        )

    # Ici, on teste la vue kandidaten_list. 
    # On utilise le client pour faire une requête GET, puis on vérifie le code de statut de la réponse.
    def test_kandidaten_list(self):
        response = self.client.get(reverse('kandidat-all', args=[self.kandidat1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test de la vue kandidaten_detail. 
    # C'est très similaire au test précédent.
    def test_kandidaten_detail(self):
        response = self.client.get(reverse('kandidat-all', kwargs={'id': self.kandidat1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Ici, on teste la vue kandidat_add. 
    # On crée une nouvelle instance de Kandidat en utilisant une requête POST. 
    # On vérifie ensuite le code de statut de la réponse.
    def test_kandidat_add(self):
        data = {
            "Vorname": "New",
            "Nachname": "Kandidat",
            "geschlecht": "M",
            "email": "newkandidat@example.com",
            "Nummer": "1122334455",
            "Beschreibung": "New Test Candidate",
            "ist_erwachsene": True
        }
        response = self.client.post(reverse('kandidat-add'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test de la vue kandidat_update. 
    # On met à jour une instance de Kandidat existante avec une requête PUT, 
    # puis on vérifie le code de statut de la réponse.
    def test_kandidat_update(self):
        data = {
            "Vorname": "Updated",
            "Nachname": "Kandidat",
            "geschlecht": "F",
            "email": "updatedkandidat@example.com",
            "Nummer": "1122334455",
            "Beschreibung": "Updated Test Candidate",
            "ist_erwachsene": False
        }
        response = self.client.put(reverse('kandidat-update', kwargs={'id': self.kandidat1.id}), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Ici, on teste la vue kandidat_delete. 
    # On supprime une instance de Kandidat avec une requête GET (en utilisant l'URL appropriée), 
    # puis on vérifie le code de statut de la réponse.
    def test_kandidat_delete(self):
        response = self.client.get(reverse('kandidat-delete', kwargs={'id': self.kandidat1.id}))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    # Test de la vue kandidat_delete_all. 
    # On supprime toutes les instances de Kandidat avec une requête GET, 
    # puis on vérifie le code de statut de la réponse.
    def test_kandidat_delete_all(self):
        response = self.client.get(reverse('kandidat-delete-all'))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
