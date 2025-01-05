from django.contrib import admin
from .models import Habito
from .models import Registro
from .models import Notificacion
# Register your models here.
admin.site.register(Habito)
admin.site.register(Registro)
admin.site.register(Notificacion)