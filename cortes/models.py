from django.db import models

class Corte(models.Model):
    imagem = models.ImageField(upload_to='cortes/')
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.descricao or f"Corte {self.id}"