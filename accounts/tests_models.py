from django.test import TestCase
from accounts.models import User
# Create your tests here.
class UserTest(TestCase):
    def create_user(self, email="ajay@test.com",first_name='Ajay',last_name='Ram',gender='M',password='1234asdf'):
        user=User.objects.create_user(email=email,first_name=first_name,last_name=last_name,username=email)
        return user

    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), str(user.pk))