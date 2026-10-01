from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sbranch=models.CharField(max_length=100)
    sname=models.CharField(max_length=100)
    Scontact=models.IntegerField()
    Semail=models.CharField(max_length=100)
    spassword=models.CharField(max_length=100)
    def __str__(self):
        return self.sname