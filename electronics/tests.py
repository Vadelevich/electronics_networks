from rest_framework import status
from rest_framework.test import APITestCase

from electronics.models import Supplier, Contact, Product
from users.models import User

data_for_responce = {"role": "FACTORY",
                     "name": "apple",
                     "contact": {
                         "email": "test@test.ru"
                     },
                     "product": {
                         "name": "appleee",
                         "model": "14",
                         "date": "2022-03-09"
                     }
                     }


class ElectronicTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(username='test1')
        self.user.set_password('123qwe456')
        self.user.save()

        response = self.client.post("/users/api/token/", {"username": "test1", "password": "123qwe456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.product = Product.objects.create(name='iphone', model='14', date='2022-03-06')
        self.contact = Contact.objects.create(email="test@test.ru")
        self.supplier = Supplier.objects.create(role="FACTORY", name="apple")

    def test_create_supplier(self):
        responce = self.client.post('/home/create_suppliers/', data_for_responce, format="json")
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)

    def test_update_supplier(self):
        data = {
            "role": "FACTORY",
            "name": "apple"
        }
        responce = self.client.put(f'/home/update_suppliers/{self.supplier.id}/', data, format="json")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        data = {
            "role": "FACTORY",
            "name": "apple",
            "debt": 43215,
            "parent": 1
        }
        responce = self.client.put(f'/home/update_suppliers/{self.supplier.pk}/', data, format="json")
        self.assertEqual(None, responce.json().get('debt'))

    def test_retrieve_supplier(self):
        responce = self.client.get(f'/home/retrive_suppliers/{self.supplier.pk}/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_list_supplier(self):
        responce = self.client.get(f'/home/list_suppliers/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_destroy_supplier(self):
        responce = self.client.delete(f'/home/destroy_suppliers/{self.supplier.pk}/')
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_contact(self):
        data = {
            "email": "test@test.ru",
            "country": "Russia",
            "city": "Moscow",
            "street": "first",
            "house_number": 1
        }
        responce = self.client.put(f'/home/update_contact_suppliers/{self.contact.pk}/', data)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        data = {
            "name": "iphone",
            "model": "13",
            "date": "2020-03-06"
        }
        responce = self.client.put(f'/home/update_product_suppliers/{self.product.pk}/', data)
