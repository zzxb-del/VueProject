from django.db import models

class Class_info(models.Model):
    class_number = models.CharField(max_length=32)
    class_name = models.CharField(max_length=32)
    rx_time = models.DateField()
    yx = models.CharField(max_length=32)

# Create your models here.
