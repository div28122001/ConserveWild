from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cn=models.PositiveBigIntegerField(default=909)
    address=models.TextField(default="INDIA")
    pimg=models.ImageField(upload_to="pimg")
    updated_on=models.DateTimeField(auto_now=True)