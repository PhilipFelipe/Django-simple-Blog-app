from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # unique = não se repete na tabela
    # www.meusite.com.br/blog/introducao-ao-django - slug
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()  # Não tem tamanho máximo
    created = models.DateTimeField(auto_now_add=True)
    # Adiciona automaticamente a data e a hora de quando foi criado o artigo
    updated = models.DateTimeField(auto_now=True)
    # A cada modificação em um artigo, atualiza o campo updated automaticament

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
