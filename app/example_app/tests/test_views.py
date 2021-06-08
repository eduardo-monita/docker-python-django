from django.test import TestCase

from example_app.models import Client

class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name="Eduardo Monita Dias", cpf="44692902893", birth_date="2000-06-24", active=True)

    def test_index_loads_properly(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)

    def test_client_detail(self):
        client = Client.objects.get(cpf="44692902893")
        response = self.client.get(f'/api/client/{client.id}/')
        self.assertEqual(response.status_code, 200)

    def test_clients_list(self):
        response = self.client.get('/api/client/')
        self.assertEqual(response.status_code, 200)
    