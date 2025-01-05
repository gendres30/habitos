from django.db import models

# Create your models here.

class Habito(models.Model):
    TIPOS_HABITO = [
        ('Estudio', 'Estudio'),
        ('Lectura', 'Lectura'),
        ('Descanso', 'Descanso'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPOS_HABITO)
    meta_diaria = models.FloatField(help_text="Meta diaria en horas")
    estado = models.BooleanField(default=True)  # Activo o Inactivo

    def __str__(self):
        return self.nombre


class Registro(models.Model):
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name='registros')
    fecha = models.DateField()
    cantidad_completada = models.FloatField(help_text="Cantidad completada en horas")

    def __str__(self):
        return f"{self.habito.nombre} - {self.fecha}"


class Notificacion(models.Model):
    habito = models.OneToOneField(Habito, on_delete=models.CASCADE, related_name='notificacion')
    hora = models.TimeField()
    frecuencia = models.CharField(max_length=20, choices=[('Diaria', 'Diaria'), ('Semanal', 'Semanal')])

    def __str__(self):
        return f"Notificación para {self.habito.nombre}"