from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:slug>/',views.paginas,name="paginas"),
]
