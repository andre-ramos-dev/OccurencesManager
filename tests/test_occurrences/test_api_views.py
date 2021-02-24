import pytest
from django.urls import reverse

from occurrences.models import Occurrence


class TestOccurrencesApiViews:

    @pytest.fixture(autouse=True)
    def setUp(self, transactional_db, client, user, superuser, category, occurrence):
        self.user = user
        self.superuser = superuser
        self.client = client
        self.category = category
        self.occurrence = occurrence

    # --------------------- Test Create --------------------------
    def test_create_occurrence(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'location': '{"longitude": 7.5556, "latitude": 37.0109}',
            'description': 'some description',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 201
        assert Occurrence.objects.get(author=self.user)

    def test_create_occurrence_not_logged(self):
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'location': '{"longitude": 7.5556, "latitude": 37.0109}',
            'description': 'some description',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 401

    def test_create_occurrence_wrong_parameters(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'location': {"longitude": 7.5556, "latitude": 37.0109},
            'description': 'some description',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_create_occurrence_no_category(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        data = {
            'location': {"longitude": 7.5556, "latitude": 37.0109},
            'description': 'some description',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_create_occurrence_no_location(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'description': 'some description',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_create_occurrence_wrong_status(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'location': '{"longitude": 7.5556, "latitude": 37.0109}',
            'description': 'some description',
            'status': 'some_status'
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_create_occurrence_unauthorized_status(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'location': '{"longitude": 7.5556, "latitude": 37.0109}',
            'description': 'some description',
            'status': 'solved'
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_create_occurrence_authorized_status(self):
        self.client.force_login(self.superuser)
        url = reverse('occurrences-list')
        data = {
            'category': self.category.id,
            'location': '{"longitude": 7.5556, "latitude": 37.0109}',
            'description': 'some description',
            'status': 'solved'
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 201

    # --------------------- Test Get Occurrences --------------------------
    def test_get_all_occurrences(self):
        self.client.force_login(self.user)
        url = reverse('occurrences-list')
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data[0]['id'] == self.occurrence.id

    def test_get_all_occurrences_without_login(self):
        url = reverse('occurrences-list')
        response = self.client.get(url)
        assert response.status_code == 401
