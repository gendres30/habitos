from django import forms
from .models import Habito, Registro, Notificacion

# Formulario para Hábito
class HabitoForm(forms.ModelForm):
    class Meta:
        model = Habito
        fields = '__all__'

# Formulario para Registro
class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'

# Formulario para Notificación
class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = '__all__'
