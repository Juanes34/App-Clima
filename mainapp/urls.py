from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="inicio"),
    path('',views.index,name="busqueda")
]
