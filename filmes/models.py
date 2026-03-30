from django.db import models

class Filme(models.Model):
    STATUS_CHOICES = [
        ('A', 'Assistido'),
        ('N', 'Não Assistido'),
    ]

    titulo = models.CharField(max_length=255) 
    status = models.CharField(
        max_length=1, 
        choices=STATUS_CHOICES, 
        default='N'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.titulo
