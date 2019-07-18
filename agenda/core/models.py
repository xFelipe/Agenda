from django.db import models


class Contact(models.Model):

    class Meta:
        db_table = 'contact'

    KINDS = (
        ('email', 'email'),
        ('celular', 'celular'),
        ('fixo', 'fixo'),
    )

    nome = models.CharField(max_length=100)
    canal = models.CharField(max_length=10, choices=KINDS)
    valor = models.CharField(max_length=100)
    obs = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
