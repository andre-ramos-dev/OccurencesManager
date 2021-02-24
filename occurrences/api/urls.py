from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from occurrences.api.views import OccurrenceViewSet

router = DefaultRouter()
router.register(r'occurrences', OccurrenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
