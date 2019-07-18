from rest_framework.test import APITestCase
from .models import Contact
# Create your tests here.


class ListTest(APITestCase):
    def setUp(self):
        data = {
            "nome": "teste1",
            "canal": "celular",
            "valor": "1111111111",
            "obs": "Observação 1"
        }
        self.client.post('/', data, format='json')
        self.client.post('/', data, format='json')
        self.response = self.client.get('/', format='json')

    def test_list_status_code(self):
        self.assertEqual(200, self.response.status_code)


class CreateTest(APITestCase):
    def setUp(self):
        data = {
                "nome": "teste1",
                "canal": "celular",
                "valor": "1111111111",
                "obs": "Observação 1"
            }
        self.response = self.client.post('/', data, format='json')

    def test_create_status_code(self):
        self.assertEqual(201, self.response.status_code)

    def test_contact_has_created(self):
        self.assertEqual(1, Contact.objects.count())


class ReadTest(APITestCase):
    def setUp(self):
        self.data = {
            "nome": "teste1",
            "canal": "celular",
            "valor": "1111111111",
            "obs": "Observação 1",
        }
        self.client.post('/', self.data, format='json')
        self.response = self.client.get('/1/', format='json')

    def test_read(self):
        self.assertEqual(1, self.response.data['id'])
        response_items = self.response.data.items()
        for field in self.data.items():
            with self.subTest():
                self.assertIn(field, response_items)


class UpdateTest(APITestCase):
    def setUp(self):
        self.data = {
            "nome": "teste1",
            "canal": "celular",
            "valor": "1111111111",
            "obs": "Observação 1",
        }
        self.client.post('/', self.data, format='json')
        self.data['canal'] = 'email'
        self.data['valor'] = '22222222'
        del(self.data['obs'])
        self.client.put('/1/', self.data)
        self.updated_contact = Contact.objects.first()

    def test_update(self):
        self.assertEqual(1, self.updated_contact.id)
        self.assertEqual('email', self.updated_contact.canal)
        self.assertEqual('22222222', self.updated_contact.valor)


class DeleteTest(APITestCase):
    def setUp(self):
        self.data = {
            "nome": "teste1",
            "canal": "celular",
            "valor": "1111111111",
            "obs": "Observação 1",
        }
        self.client.post('/', self.data, format='json')

    def test_delete(self):
        self.assertEqual(1, Contact.objects.count())
        response = self.client.delete('/1/', self.data)
        self.assertEqual(0, Contact.objects.count())

    def test_delete_error(self):
        response = self.client.delete('/2/', self.data)
        self.assertEqual(404, response.status_code)