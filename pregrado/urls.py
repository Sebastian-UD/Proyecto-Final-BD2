from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_pregrados, name='get_pregrados'),
    path('create', views.create_pregrado, name='create_pregrado')
    #path('create', views.create_sede, name='create_sedes'),
    #path('detail/<int:codigo>', views.sede_detail, name='sede_detail'),
    #path('delete/<int:codigo>', views.delete_sede, name='delete_sede')
]