from django.test import TestCase,Client
from accounts.models import User
from rest_framework_jwt.settings import api_settings
from movies_info.models import *
from django.db import IntegrityError
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class BaseCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email="ajay@test.com", first_name='Ajay', last_name='Ram',username="ajay@test.com",password='password_hash')
        self.movie=Movies.objects.create(movie_name="avengers",movie_genre="Action",user=self.user,movie_year="2012")
        payload = jwt_payload_handler(self.user)
        self.auth_token = 'YNF {}'.format(jwt_encode_handler(payload))


    def tearDown(self):
        self.user.delete()
        self.movie.delete()

