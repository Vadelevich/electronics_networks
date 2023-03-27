from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(username='test1')
        self.user.set_password('123qwe456')
        self.user.status = User.STATUS_INACTIVE
        self.user.save()

        response = self.client.post("/users/api/token/", {"username": "test1", "password": "123qwe456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_create_user(self):
        response = self.client.post(path="/users/create_user/",
                                    data={"username": "oliya2023@test.ru", "password": "123qwe456"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post('/users/create_user/', {"username": "oliya2023@test.ru", "password": "123qwe456"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_data = {
            "username": [
                "Пользователь с таким именем уже существует."
            ]
        }
        self.assertEqual(response.json(), expected_data)

    def test_permissions(self):
        responce = self.client.get(path='/home/list_suppliers/')
        self.assertEqual(responce.status_code,status.HTTP_403_FORBIDDEN)
