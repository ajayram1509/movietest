import nose.tools as nt
from .test import BaseCase
import json
import sys

class Testaccounts(BaseCase):

    def test_signUp(self):
        path = '/accounts/Signup/'
        data = json.dumps({'FirstName':'ajay','LastName':'ram','Email':'ajay.test@testtest.com','Password':'Hello@123'})
        response = self.client.post(path, data, content_type='application/json')
        json_response = json.loads(response.content)
        status = json_response["status"]
        if status==True:
            sys.stderr.write("\n Signup test: pass \n")
        else:
            sys.stderr.write("\n error \n")
        nt.assert_equal(status, True)

    def test_login(self):
        self.test_signUp()
        path = '/accounts/Login/'
        data = json.dumps({'Email':'ajay.test@testtest.com','Password':'Hello@123'})
        response = self.client.post(path, data, content_type='application/json')
        json_response = json.loads(response.content)
        status = json_response["status"]
        if status==True:
            sys.stderr.write("\n Login test: pass \n")
        else:
            sys.stderr.write("\n error \n")
        nt.assert_equal(status, True)