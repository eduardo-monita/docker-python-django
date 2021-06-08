from django.test import TestCase

from example_app.models import Client

class ModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name="Eduardo Monita Dias", cpf="44692902893", birth_date="2000-06-24", active=True)
        Client.objects.create(name="Ana Carolina de Matos Brunetti", cpf="49099961848", birth_date="2001-02-23", active=True)

    def test_cpf_max_length(self):
        client = Client.objects.get(cpf="44692902893")
        max_length = client._meta.get_field('cpf').max_length
        self.assertEquals(max_length, 11)