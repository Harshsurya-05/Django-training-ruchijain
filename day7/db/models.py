from django.db import models

class Employee(models.Model):
    
    Eno = models.IntegerField()
    Ename = models.CharField(max_length=100)
    Esalary = models.CharField(max_length=100)

    def __str__(self):
        return self.Ename


