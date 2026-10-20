from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits = 8, decimal_places = 2)
    data_publicacao = models.DateField()
    sinopse = models.TextField()
    
    def __str__(self):
        return self.titulo
