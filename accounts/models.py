from django.db import models
from django.contrib.auth.models import User as user

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(user):
    pass


    def __str__(self):
        return str(self.pk)

    def json(self):
        ret={}
        ret['user_id']=self.pk
        ret['first_name']=self.first_name
        ret['last_name']=self.last_name
        ret['email']=self.email
        return ret

