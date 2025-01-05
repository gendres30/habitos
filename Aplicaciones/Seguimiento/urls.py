from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Hábito
    path('', views.inicio, name='inicio'),
    path('habitos/', views.listar_habitos, name='listar_habitos'),
    path('habitos/crear/', views.crear_habito, name='crear_habito'),
    path('habitos/editar/<int:id>/', views.editar_habito, name='editar_habito'),
    path('habitos/eliminar/<int:id>/', views.eliminar_habito, name='eliminar_habito'),
    
    path('registros/', views.listar_registros, name='listar_registros'),
    path('registros/crear/', views.crear_registro, name='crear_registro'),
    path('registros/editar/<int:id>/', views.editar_registro, name='editar_registro'),
    path('registros/eliminar/<int:id>/', views.eliminar_registro, name='eliminar_registro'),
   
    path('notificaciones/', views.listar_notificaciones, name='listar_notificaciones'),
    path('notificaciones/crear/', views.crear_notificacion, name='crear_notificacion'),
    path('notificaciones/editar/<int:pk>/', views.editar_notificacion, name='editar_notificacion'),
    path('notificaciones/eliminar/<int:pk>/', views.eliminar_notificacion, name='eliminar_notificacion'),

]

