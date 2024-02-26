from django.urls import path
from . import views

urlpatterns = [
    path("", views.AuthUserView.as_view(), name='start'),
    path("code/", views.AuthInputCodeView.as_view(), name='code'),
    path("code/retry", views.SendCode.as_view(), name='retry_send_code')
]
