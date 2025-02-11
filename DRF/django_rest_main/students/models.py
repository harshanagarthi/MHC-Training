from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    branch = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.name}, {self.age}, {self.branch}'