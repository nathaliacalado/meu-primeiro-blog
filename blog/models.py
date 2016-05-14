from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_de_criacao = models.DateTimeField(
            default=timezone.now)
    data_de_publicacao = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.data_de_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
# Create your models hereself.
