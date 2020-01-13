from django.db import models
import logging

#log = logging()


# Create your models here.
#class Equipment(models.Model):
#   name = ...  quantity = ...


class User(models.Model):
    name = models.CharField(max_length= 120, verbose_name=u"Nome do Usuario")
    email = models.EmailField(max_length= 250, verbose_name=u"Email do Usuario")
    cpf = models.CharField(max_length=120, verbose_name=u"Cpf do Usuario")
    matricula = models.CharField(max_length=120, verbose_name=u"Matricula do Usuario")
    password = models.CharField(max_length= 120, verbose_name=u"Password do Usuario")

   #def save(self):
   #    if self.cpf_is_valid():
   #        return self.save()
   #    return self.messages(log.ERROR, "Invalid CPF")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

