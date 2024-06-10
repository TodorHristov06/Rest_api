from django.db import models

class Computer(models.Model):
    url = models.URLField(unique=True)
    processor = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.processor} | {self.gpu} | {self.motherboard} | {self.ram}"

# Create your models here.
