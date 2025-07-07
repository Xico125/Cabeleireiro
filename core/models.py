from django.db import models

class Barbeiro(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='barbeiros/')

    def __str__(self):
        return self.nome