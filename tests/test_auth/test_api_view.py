import pytest
from django.contrib.auth.models import User
from django.urls import reverse


class TestAuthApiViews:

    @pytest.fixture(autouse=True)
    def setUp(self, transactional_db, client):
        self.client = client
        # self.client.login(username=user.username, password='test')

    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'test1',
            'password': 'test1',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 201
        assert User.objects.get(username='test1')

    def test_register_user_no_password(self):
        url = reverse('register')
        data = {
            'username': 'test1',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_register_user_no_username(self):
        url = reverse('register')
        data = {
            'username': 'test1',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400
