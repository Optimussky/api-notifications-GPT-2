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
    #dataSystem = models.ForeignKey("notification.DataSystem", on_delete=models.CASCADE)# Se evita tener que usar jeraquía al crear clases
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    email = models.EmailField()
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

"""
class DataSystem(models.Model):
    
    name = models.CharField(max_length=255)

"""

"""
Formas en las que le puedo dar sentido a crear la clase DataSystem

- Necesito crear una clase(Modelo) con x número de campos
- El propósito de esos campos es... (comprobar algo que ya existe, o insertar algo nuevo)


# Caso: Comprobar algo que ya existe:
    - Después de crear mi clase sería necesario invocarla a través de: serializers.py
    - Usar el serializers.py invocando SerializerDataSystem dentro views.py o tal vez crear otro archivo tipo manager.py
    - Dentro del manager.py(views.py) hacer una consulta que pregunte:
        - si los datos del modelo DataSystem coinciden con la info(campos) de Notification 

"""