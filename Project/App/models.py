from django.db import models

# Create your models here.
class Contact_Detail(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    def __str__(self):
        return f"{self.image}"
