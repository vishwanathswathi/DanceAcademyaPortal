from django.db import models
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=234)
    mobile= models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=234)
    def __str__(self):
        return self.name +self.mobile+self.email+self.message

class music(models.Model):
    image=models.FileField(upload_to='music/')
    # def __str__(self):
    #     return self.image

class bharatanatyam(models.Model):
    image=models.FileField(upload_to='bharatanatyam/')
    # def __str__(self):
    #     return self.image

class kuchipudi(models.Model):
  image=models.FileField(upload_to='kuchipudi/')
  # def __str__(self):
  #         return self.image
class westerndance(models.Model):
  image=models.FileField(upload_to='westerndance/')
  # def __str__(self):
  #         return self.image


class guitar(models.Model):
  image=models.FileField(upload_to='guitar/')
  # def __str__(self):
  #         return self.image

class keyboard(models.Model):
  image=models.FileField(upload_to='keyboard/')
  # def __str__(self):
  #         return self.image

class video(models.Model):
    video=models.FileField(upload_to="video/%y")