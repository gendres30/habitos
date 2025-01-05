from django.shortcuts import render, get_object_or_404, redirect
from .models import Registro, Habito
from .forms import RegistroForm
from .forms import HabitoForm
from .models import Notificacion
from .forms import NotificacionForm

# Create your views here.


# Listar Hábitos
def listar_habitos(request):
    habitos = Habito.objects.all()
    return render(request, 'habitos/listar_habitos.html', {'habitos': habitos})

# Crear Hábito
def crear_habito(request):
    if request.method == 'POST':
        form = HabitoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_habitos')
    else:
        form = HabitoForm()
    return render(request, 'habitos/crear_habito.html', {'form': form})

# Editar Hábito
def editar_habito(request, id):
    habito = get_object_or_404(Habito, pk=id)
    if request.method == 'POST':
        form = HabitoForm(request.POST, instance=habito)
        if form.is_valid():
            form.save()
            return redirect('listar_habitos')
    else:
        form = HabitoForm(instance=habito)
    return render(request, 'habitos/editar_habito.html', {'form': form})

# Eliminar Hábito
def eliminar_habito(request, id):
    habito = get_object_or_404(Habito, pk=id)
    if request.method == 'POST':
        habito.delete()
        return redirect('listar_habitos')
    return render(request, 'habitos/eliminar_habito.html', {'habito': habito})




# Listar Registros
def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'registros/listar_registros.html', {'registros': registros})

# Crear Registro
def crear_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')  # Redirige al listado de registros
    else:
        form = RegistroForm()
    return render(request, 'registros/crear_registro.html', {'form': form})

# Editar Registro
def editar_registro(request, id):
    registro = get_object_or_404(Registro, pk=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'registros/editar_registro.html', {'form': form})

# Eliminar Registro
def eliminar_registro(request, id):
    registro = get_object_or_404(Registro, pk=id)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar_registros')
    return render(request, 'registros/eliminar_registro.html', {'registro': registro})


# Listar notificaciones
def listar_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'notificaciones/listar.html', {'notificaciones': notificaciones})

# Crear una nueva notificación
def crear_notificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notificaciones')
    else:
        form = NotificacionForm()
    return render(request, 'notificaciones/crear.html', {'form': form})

# Editar una notificación existente
def editar_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('listar_notificaciones')
    else:
        form = NotificacionForm(instance=notificacion)
    return render(request, 'notificaciones/editar.html', {'form': form, 'notificacion': notificacion})

# Eliminar una notificación
def eliminar_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        notificacion.delete()
        return redirect('listar_notificaciones')
    return render(request, 'notificaciones/eliminar.html', {'notificacion': notificacion})


#inicio
#def inicio(request):
#    habitos = [
 #       {'nombre': 'Estudio', 'progreso': 80, 'meta': '2 horas/día'},
  #      {'nombre': 'Lectura', 'progreso': 50, 'meta': '30 min/día'},
   #     {'nombre': 'Ejercicio', 'progreso': 90, 'meta': '1 hora/día'},
    #]
    #historial = [
     #   {'habito': 'Estudio', 'fecha': '2025-01-01', 'progreso': '2 horas'},
      #  {'habito': 'Lectura', 'fecha': '2025-01-02', 'progreso': '15 min'},
       # {'habito': 'Ejercicio', 'fecha': '2025-01-03', 'progreso': '1 hora'},
    #]
    #return render(request, 'inicio.html', {'habitos': habitos, 'historial': historial})

def inicio(request):
    # Obtener hábitos activos
    habitos = Habito.objects.filter(estado=True)

    # Calcular progreso para cada hábito por tipo
    resumen_habitos = []
    for habito in habitos:
        registros = habito.registros.all()  # Relación inversa desde `related_name`
        progreso_total = sum([registro.cantidad_completada for registro in registros])
        meta_total = habito.meta_diaria * len(registros)
        progreso_porcentaje = (
            (progreso_total / meta_total) * 100 if meta_total > 0 else 0
        )
        resumen_habitos.append({
            'nombre': habito.nombre,
            'tipo': habito.tipo,
            'meta_diaria': habito.meta_diaria,
            'progreso_total': round(progreso_porcentaje, 2),
        })

    # Obtener historial de registros recientes (últimos 10)
    historial = Registro.objects.order_by('-fecha')[:10]

    return render(request, 'inicio.html', {
        'resumen_habitos': resumen_habitos,
        'historial': historial,
    })