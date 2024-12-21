from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Designation = models.CharField(max_length=100)
    Start_date = models.DateField()
    Salary = models.DecimalField(max_digits=10,decimal_places=2)
    Photo = models.ImageField(upload_to='image/',null=True)
    def __str__(self):
        return self.Name
    
