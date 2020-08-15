from django.db import models

class userinfo(models.Model):
    f_name= models.CharField(max_length=200)
    l_name= models.CharField(max_length=200)
    ph_no= models.BigIntegerField()
    email= models.EmailField()
    gender= models.CharField(max_length=15)

    def __str__(self):
        return self.f_name + ' ' + self.l_name
    