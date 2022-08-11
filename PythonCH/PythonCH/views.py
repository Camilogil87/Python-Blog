from cgitb import html
from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template
from django.template import Context
from django.template import loader
from MTV1.models import familiares

def hello(request):
    return HttpResponse('Hola papi')#saludo

def Nombre(response,nombre):
    texto=f'Mi nombre es: <br><br> {nombre}'
    return HttpResponse(texto)


def primertemplate(response):
    htmlcamilo=open(r'C:\Users\user\OneDrive\Escritorio\Python Proyecto Final\PythonCH\PythonCH\Plantillas\template.html')
    miplantilla=Template(htmlcamilo.read())

    htmlcamilo.close()

    contextocamilo=Context()

    midocumento=miplantilla.render(contextocamilo)

    return HttpResponse(midocumento)

def segundotemplate(response):
    nom= 'Camilo'
    apellido='Gil'

    dicc= {'nombre': nom, 'apellido': apellido}

    htmlcamilo2=open(r'C:\Users\user\OneDrive\Escritorio\Python Proyecto Final\PythonCH\PythonCH\Plantillas\template.html')
    miplantilla2=Template(htmlcamilo2.read())

    htmlcamilo2.close()

    contextocamilo2=Context()

    midocumento2=miplantilla2.render(contextocamilo2)

    return HttpResponse(midocumento2)

def tercertemplate(response,nombre):
    dicc= {'fecha_actual': datetime.now(), 'usuario':nombre}

    htmlcamilo3=open(r'C:\Users\user\OneDrive\Escritorio\Python Proyecto Final\PythonCH\PythonCH\Plantillas\template.html')
    miplantilla3=Template(htmlcamilo3.read())

    htmlcamilo3.close()

    contextocamilo3=Context(dicc)

    midocumento3=miplantilla3.render(contextocamilo3)

    return HttpResponse(midocumento3)

def cuartotemplate(response):
    lista1=[2,5,6,8,4]
    dicc= {'fecha_actual': datetime.now(), 'notas':lista1, 'usuario':'Camilo'}

    htmlcamilo4=open(r'C:\Users\user\OneDrive\Escritorio\Python Proyecto Final\PythonCH\PythonCH\Plantillas\template.html')
    miplantilla4=Template(htmlcamilo4.read())

    htmlcamilo4.close()

    contextocamilo4=Context(dicc)

    midocumento4=miplantilla4.render(dicc)

    return HttpResponse(midocumento4)

def quintotemplate(response):
    
    lista1=[2,5,6,8,4]
    dicc= {'fecha_actual': datetime.now(), 'notas':lista1, 'usuario':'Camilo'}

    miplantilla5=loader.get_template('template.html')

    midocumento4=miplantilla5.render(dicc)

    return HttpResponse(midocumento4)

def familiares3(response):
    familiar1=familiares(nombre='Camilo', dni=1929383029,Fecha_nacimiento='1994-11-14')
    familiar1.save()
    familiar2=familiares(nombre='May', dni=38929837,Fecha_nacimiento='1976-8-16')
    familiar2.save()
    familiar3=familiares(nombre='David', dni=84939384,Fecha_nacimiento='1996-1-29')
    familiar3.save()
    doctexto=f'nombre:{familiar1.nombre} <br> dni:{familiar1.dni} <br> Fecha_nacimiento:{familiar1.Fecha_nacimiento} <br><br> nombre:{familiar2.nombre} <br> dni= {familiar2.dni} <br> Fecha_nacimiento:{familiar2.Fecha_nacimiento} <br><br> nombre:{familiar3.nombre} <br> dni={familiar3.dni} <br> Fecha_nacimiento={familiar3.Fecha_nacimiento}'
    return HttpResponse(doctexto)

