from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from kandidat.forms import RegisterForm
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.status import HTTP_200_OK

class RegisterViewTest(TestCase):
    def setUp(self):
        # Initialiser le client de test
        self.client = Client()

        # URL de la vue à tester
        self.register_url = reverse('register')

    def test_register_user(self):
        # Créer des données de formulaire de test
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'confirm': 'testpassword123',
        }

        # Envoyer une requête POST à la vue avec les données du formulaire
        response = self.client.post(self.register_url, data)

        # Vérifier que l'utilisateur a été créé
        self.assertEqual(get_user_model().objects.count(), 1)

        # Vérifier que la vue redirige à la page d'accueil après une inscription réussie
        self.assertRedirects(response, reverse('login'))

    def test_register_user_with_password_mismatch(self):
        # Créer des données de formulaire où le mot de passe et la confirmation ne correspondent pas
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'confirm': 'wrongpassword',
        }

        # Envoyer une requête POST à la vue avec les données du formulaire
        response = self.client.post(self.register_url, data)

        # Vérifier que l'utilisateur n'a pas été créé
        self.assertEqual(get_user_model().objects.count(), 0)

        # Vérifier que la vue renvoie le bon template avec l'erreur
        self.assertTemplateUsed(response, 'kandidat/register.html')
        self.assertTrue(response.context['error'])

################################################# ceci est la partie des tests du login


class SigninViewTest(TestCase):
    def setUp(self):
        # Initialiser le client de test
        self.client = Client()

        # URL de la vue à tester
        self.signin_url = reverse('login')

        # Créer un utilisateur de test
        self.testuser = get_user_model().objects.create(
            username='testuser', password='testpassword123')

    def test_signin_user(self):
        # Créer des données de formulaire de test
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }

        # Envoyer une requête POST à la vue avec les données du formulaire
        response = self.client.post(self.signin_url, data)

        # Vérifier que la vue redirige à la page d'accueil après une connexion réussie
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_signin_user_with_incorrect_password(self):
        # Créer des données de formulaire où le mot de passe est incorrect
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }

        # Envoyer une requête POST à la vue avec les données du formulaire
        response = self.client.post(self.signin_url, data)

        # Vérifier que la vue renvoie le bon template avec l'erreur
        self.assertTemplateUsed(response, 'kandidat/login.html')