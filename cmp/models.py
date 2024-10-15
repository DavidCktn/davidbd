from typing import Iterable
from django.db import models
from bases.models import ClaseModelo


class Proveedor(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        unique=True
    )
    direccion = models.CharField(
        max_length=250,
        null=True, blank=True
    )
    contacto = models.CharField(
        max_length=100
    )
    telefono = models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Proveedores"