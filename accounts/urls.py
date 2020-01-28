from django.conf.urls import url
from .import views




urlpatterns = [
   url(r'Signup/',views.Signup.as_view(),name='signup_user'),
   url(r'Login/',views.Login.as_view(),name='login_user'),
 ]