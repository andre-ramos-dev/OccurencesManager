import pytest
from django.contrib.auth import get_user_model
from occurrences.models import Category, Occurrence
from django.contrib.gis.geos import Point

@pytest.fixture
def enable_db_access(db):
    pass


@pytest.fixture
def user():
    user = get_user_model().objects.create(username='test', password='test')
    return user

@pytest.fixture
def superuser():
    user = get_user_model().objects.create(username='adm', password='adm', is_superuser=True)
    return user

@pytest.fixture
def category():
    category = Category.objects.create(type='CONSTRUCTION', description='Planned RoadWork Events')
    return category

@pytest.fixture
def occurrence(superuser, category):
    occurrence = Occurrence.objects.create(
                                author=superuser,
                                category=category,
                                location=Point(7.2344, 37.5529),
                                status = 'to_validate',
                                description='some description',
                            )
    return occurrence