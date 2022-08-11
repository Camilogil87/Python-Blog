"""PythonCH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PythonCH.views import familiares3 #importar todo lo necesario para ejecutar la web
from PythonCH.views import cuartotemplate# funciones definidas en la pestaña views
from PythonCH.views import tercertemplate
from PythonCH.views import segundotemplate
from PythonCH.views import Nombre
from PythonCH.views import hello
from PythonCH.views import primertemplate
from PythonCH.views import quintotemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello),
    path('minombre/<nombre>', Nombre),
    path('templatecamilo/', primertemplate),
    path('templatecamilo2/', segundotemplate),
    path('cuartotemplate/', cuartotemplate), #el str de la linea 32 deberia estar al ultimo para no tomar valor de la URL
    path('quintotemplate/', quintotemplate),
    path('familiares3/',familiares3),
    path('<str:nombre>/', tercertemplate),#se le asigno un parametro para recibir cualquier nombrede la URL    
]
