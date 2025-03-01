# residuos/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Residuo, Coleta, Recompensa

class ResiduoTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.residuo = Residuo.objects.create(
            usuario=self.user,
            tipo='Plástico',
            quantidade=1.0,
            pontos=10
        )
        self.coleta = Coleta.objects.create(
            residuo=self.residuo,
            data_coleta='2025-01-01',
            localizacao='Local Padrão'
        )
        self.recompensa = Recompensa.objects.create(
            nome='Brinquedo',
            descricao='Um brinquedo divertido',
            pontos_necessarios=100
        )

    def test_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sustentabilidade Divertida')

    def test_registrar_residuo_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('registrar_residuo'))
        self.assertEqual(response.status_code, 200)

    def test_listar_coletas_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('listar_coletas'))
        self.assertEqual(response.status_code, 200)

    def test_catalogo_recompensas_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalogo_recompensas'))
        self.assertEqual(response.status_code, 200)
