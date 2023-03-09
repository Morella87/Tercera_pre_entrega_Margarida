from django.shortcuts import render

from Preentrega3.forms import (CursoFormulario, EntregablesFormulario,
                               EstudiantesFormulario, ProfesorFormulario)
from Preentrega3.models import Curso, Entregable, Estudiante, Profesor

# Creacion de vistas.

def inicio(request):
    return render(request, 'inicio.html')

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudiantesFormulario(request.POST) #Aca llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid: #si paso la validacion de django

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                email=informacion['email'])
            
            estudiante.save()
        
            return render(request, 'inicio.html') #vuelve al inicio 
    else: 
        miFormulario = EstudiantesFormulario() #formulario vacio para construir el html

    return render(request, 'estudiantes.html',{'miFormulario':miFormulario})


def entregables(request):
    if request.method == 'POST':
        miFormulario = EntregablesFormulario(request.POST) #Aca llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid: #si paso la validacion de django

            informacion = miFormulario.cleaned_data

            entregable = Entregable (nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'],
                entregado=informacion['entregado'])
            
            entregable.save()
        
            return render(request, 'inicio.html') #vuelve al inicio 
    else: 
        miFormulario = EntregablesFormulario() #formulario vacio para construir el html

    return render(request, 'entregables.html',{'miFormulario':miFormulario})

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST) #Aca llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid: #si paso la validacion de django

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
        
            return render(request, 'inicio.html') #vuelve al inicio 
    else: 
        miFormulario = CursoFormulario() #formulario vacio para construir el html

    return render(request, 'cursos.html',{'miFormulario':miFormulario})

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST) #Aca llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid: #si paso la validacion de django

            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                email=informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()
        
            return render(request, 'inicio.html') #vuelve al inicio 
    else: 
        miFormulario = ProfesorFormulario() #formulario vacio para construir el html

    return render(request, 'profesores.html',{'miFormulario':miFormulario})

#def busquedaCamada(request):
    #return render(request, 'busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'inicio.html', {'cursos':cursos, 'camada':camada})

    else:
        respuesta = 'No enviaste datos'

    return render(request, 'inicio.html', {'respuesta':respuesta})