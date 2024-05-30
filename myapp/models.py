from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=100, blank=True,null=True)
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    dob = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True)