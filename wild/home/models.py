
# from distutils.command.upload import upload
from modulefinder import packagePathMap
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import DurationField
from django.contrib.auth.models import User


# Create your models here.
class subsscription(models.Model):
    Package=models.CharField(max_length=25)
    price=models.IntegerField()
    Duration=models.IntegerField()
    offer=models.IntegerField()


    
class pscat(models.Model):
    cat_head=models.CharField(max_length=100)
    description=models.TextField(null=True)
    bimage=models.ImageField(upload_to='pscatimg',null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.cat_head
class Post(models.Model):
    cat=models.ForeignKey(pscat,default=3,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True, null=True)
    updated_on=models.DateTimeField(auto_now=True, null=True)
    pst_title=models.CharField(max_length=25)
    pst_desc=models.TextField()
    img=models.ImageField(upload_to="pic")
    likes=models.ManyToManyField(User,related_name="user")
   
    def __str__(self):
            return self.pst_title
    

class Package(models.Model):
    p_name=models.CharField(max_length=50)
    p_desc=models.TextField()
    p_price=models.IntegerField(max_length=50)
    p_priceupd=models.DateTimeField(auto_now_add=True)
    p_image=models.ImageField(upload_to="pfps")

    def __str__(self):
        return self.p_name

class Reaction(models.Model):
    pst=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True, null=True)
    updated_on=models.DateTimeField(auto_now=True, null=True)
    Comment=models.TextField(default=0)  
    
class Contact (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sub=models.CharField(max_length=500)
    message=models.TextField(default=0)
    contactnum=models.PositiveIntegerField()
    updated_on=models.DateTimeField(auto_now_add=True, null=True)
 

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField( blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)    

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default="False")
    service=models.ForeignKey(Package,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    update_on=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username
class Room(models.Model):
    """Represents chat rooms that users can join"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name
class Order(models.Model):
    cust_id=models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids=models.CharField(max_length=250)
    product_ids=models.CharField(max_length=250)
    invoice_id=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    processed_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_id.username
