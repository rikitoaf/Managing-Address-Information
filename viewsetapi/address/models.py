from django.db import models

# Create your models here.

class Parent (models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    email_name = models.EmailField(max_length= 100)
    phone_num = models.CharField(max_length= 100,default="Individual")
    address_name = models.CharField(max_length= 100)

    def __str__(self):
        return   self.first_name
    def get_fields(self):
        return [(field.first_name(self), field.last_name(self)) for field in self.__class__._meta.fields]   


class Children (models.Model):
    parent_name = models.ForeignKey(Parent , on_delete= models.CASCADE)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
