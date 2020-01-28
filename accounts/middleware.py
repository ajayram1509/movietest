from django.contrib.auth.middleware import get_user
import time
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .utils import httpResponseBadRequest
import jwt
from rest_framework_jwt.settings import api_settings
from django.db import connection

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class AuthenticationMiddlewareJWT(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def get_jwt_user(self,request):
        user=None
        user = get_user(request)
        msg=None
        if user.is_authenticated:
            return user,msg
        jwt_authentication = JSONWebTokenAuthentication()
        token=jwt_authentication.get_jwt_value(request)
        if token:
            try:
                payload = jwt_decode_handler(token)
            except jwt.ExpiredSignature:
                msg = 'Signature has expired.'
            except jwt.DecodeError:
                msg = 'Error decoding signature.'
            except jwt.InvalidTokenError:
                msg="Invalid Token/Credentials."
            if not msg:
                user = jwt_authentication.authenticate_credentials(payload)
        return user,msg


    def __call__(self, request):

        request.user,msg=self.get_jwt_user(request)
        if msg:
            return httpResponseBadRequest(msg,message="SIGNATURE EXPIRED",status_code=401)
        response=self.get_response(request)
        if response.status_code==401:
            return httpResponseBadRequest("signature expired",message="SIGNATURE EXPIRED",status_code=401)
        return response