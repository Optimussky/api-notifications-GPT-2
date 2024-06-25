from django.db import models
import uuid

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Notification(models.Model):
    # foreingKey con dataSystem
    #dataSystem = models.ForeignKey("notification.dataSystem", on_delete=models.CASCADE)# Se evita tener que usar jeraquía al crear clases
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    email = models.EmailField()
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

"""
class dataSystem(models.Model):
    
    name = models.CharField(max_length=255)

"""