from django.shortcuts import render
from crudapp.scripts import modify_database as modify_db
from crudapp.models import Persona
from crudapp.serializer import PersonaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template import RequestContext
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def modify(request):
    """Receives a dni and returns the information"""
    dni = request.GET.get('dni')
    user = Persona.objects.get(dni=dni)
    return render(request, 'modify.html', {'user': user})


def modify_user(request):
    """ Modifying a user """

    Persona.objects.filter(dni=request.data['dni']).update(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        birth_date=request.data['birth_date'],
        address=request.data['address'],
        phone_number=request.data['phone_number']
    )
    # modify_db.update_user(request.GET.copy())


def new_user(request):
    """ Creating a new user """
    if Persona.objects.filter(dni=request.GET.get('dni')).exists():
        modify_user(request)
    else:
        Persona.objects.create(
            first_name=request.GET.get('first_name'),
            last_name=request.GET.get('last_name'),
            dni=request.GET.get('dni'),
            birth_date=request.GET.get('birth_date'),
            address=request.GET.get('address'),
            phone_number=request.GET.get('phone_number')
        )

    # modify_db.add_user(request.GET.copy())
    return render(request, 'home.html')


def view(request):
    """Receives a dni and returns the information"""
    dni = request.GET.get('dni')
    user = Persona.objects.get(dni=dni)
    return render(request, 'view.html', {'user': user})


@api_view(['GET'])
def getData(request):
    if request.method == 'GET':
        # Return all data startswith request.GET['text']
        text = request.GET['text']
        if (text.isdigit()):
            personas = Persona.objects.filter(dni__startswith=text)
        else:
            if text == '':
                personas = Persona.objects.all()
            else:
                personas = Persona.objects.filter(first_name__startswith=text)
    serializer = PersonaSerializer(personas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPersona(request):
    """ Adding a new user """
    print(request.data)
    if request.method == 'POST':
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            if Persona.objects.filter(dni=request.data['dni']).exists():
                modify_user(request)
                return Response(serializer.data, status=201)
            else:
                serializer.save()
                return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def deletePersona(request):
    """ Deleting a user from the database"""
    print(request.data)
    if request.method == 'DELETE':
        dni = request.GET['dni']
        Persona.objects.filter(dni=dni).delete()
        return Response(status=204)
    return Response(status=400)
