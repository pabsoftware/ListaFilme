from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=200)
    def __str__(self):
        return self.categoria

class Filmes(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    url_do_filme = models.URLField(max_length=500)
    titulo = models.CharField("Título do Filme",max_length=200)
    descricao = models.TextField("Descrição do Filme:")
    favorito = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
