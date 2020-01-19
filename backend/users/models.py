from django.db import models


class User(models.Model):
    username = models.CharField(max_length= 120, verbose_name=u"Nome do Usuario")
    email = models.EmailField(unique=True, verbose_name=u"Email do Usuario")
    cpf = models.CharField(max_length=120, unique=True, verbose_name=u"Cpf do Usuario")
    matricula = models.CharField(max_length=120, unique=True, blank=False, verbose_name=u"Matricula do Usuario")
    password = models.CharField(max_length= 120, verbose_name=u"Password do Usuario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    # TODO
    # Needs to create manager to validate CPF, EMAIL and encode password
    # userManager = UserManager()
    # objects = models.Manager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

