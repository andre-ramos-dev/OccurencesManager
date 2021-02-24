from django.conf.urls import url

from .views import CreateUserView, LoginUserView

urlpatterns = [
    url('auth/register/', CreateUserView.as_view(), name='register'),
    url(r'auth/login/$', LoginUserView.as_view(), name='login'),
]
