from django.shortcuts import render
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
import json
from .models import User

from .utils import validate_data,httpResponse,httpResponseBadRequest
# Create your views here.
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class Signup(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        params = json.loads(request.body)
        req = ['Email','Password','FirstName','LastName']
        error=validate_data(params, req)
        if error:
            return httpResponseBadRequest(error,"DATA MISSING")
        try:
            user=User.objects.create(email=params['Email'],first_name=params['FirstName'],last_name=params['LastName'],username=params['Email'])
            user.set_password(params['Password'])
            user.save()
            return httpResponse('User Created successfully')
        except Exception as e:
            return httpResponseBadRequest(error_description="USER ALREADY EXIST")

class Login(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        params = json.loads(request.body)
        req = ['Email','Password']
        error=validate_data(params, req)
        if error:
            return httpResponseBadRequest(error,'DATA MISSING')
        try:
            user=User.objects.get(username=params['Email'])
            if user.check_password(params['Password']):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                ret={}
                ret['Token']=token
                ret['User']=user.json()
                return httpResponse(ret)
            else:
                return httpResponseBadRequest(error_description="InCorrect Password")
        except:
            return httpResponseBadRequest(error_description="Invalid User Credentials")
