from django.db import models
from django.contrib.auth.models import User

class Movimiento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumb = models.IntegerField()
    index = models.IntegerField()
    middle = models.IntegerField()
    ring = models.IntegerField()
    pinky = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movimiento de {self.user.username} - {self.fecha}"
