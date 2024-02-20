from django.db import models

# Create your models here.
class Contact_Detail(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    def __str__(self):
        return f"{self.image}"

class Outlet(models.Model):
    outlet_main_title = models.CharField(max_length=20, null=False)
    outlet_name = models.CharField(max_length=50, null=False)
    address_line_1 = models.CharField(max_length=70, null=False)
    address_line_2 = models.CharField(max_length=70, null=False)
    address_line_3 = models.CharField(max_length=70, null=False)
    address_line_4 = models.CharField(max_length=70, null=True, blank=True)
    address_line_5 = models.CharField(max_length=70, null=True, blank=True)
    outlet_landline = models.CharField(max_length=15, null=True, blank=True)
    outlet_email = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.outlet_main_title
    
class Team_line_1(models.Model):
    Member_image = models.ImageField(upload_to='team')
    Member_name = models.CharField(max_length = 50)
    Member_title = models.CharField(max_length = 50)
    def __str__(self):
        return f"{self.Member_name} - {self.Member_title}"
    
class Team_line_2(models.Model):
    Member_image = models.ImageField(upload_to='team')
    Member_name = models.CharField(max_length = 50)
    Member_title = models.CharField(max_length = 50)
    def __str__(self):
        return f"{self.Member_name} - {self.Member_title}"