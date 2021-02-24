from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CreateUserView, LoginUserView, AuthorViewSet

router = DefaultRouter()

router.register(r'authors', AuthorViewSet)
urlpatterns = [
    # auth
    url('auth/register/', CreateUserView.as_view(), name='register'),
    url(r'auth/login/$', LoginUserView.as_view(), name='login'),
    path('', include(router.urls)),
]
