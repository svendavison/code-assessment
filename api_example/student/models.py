from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    studentId = models.IntegerField()
    

    class Meta:
        verbose_name = ("Sutdent")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name

