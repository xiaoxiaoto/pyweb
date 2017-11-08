from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection,transaction


# Create your views here.

from django.shortcuts import render
from .models import Person
from django import forms


class personBO(forms.Form):
    id=forms.CharField()
    name = forms.CharField()
    age = forms.IntegerField()

def route(request, path):
    if path == 'index':
        rows=Person.objects.raw('select * from first_person')
        for row in rows:
            print(row.id)

        cursor=connection.cursor()
        cursor.execute("select * from first_person")
        rows=cursor.fetchall()
        for row in rows:
            print(row)

        persons = Person.objects.all()
        return render(request, 'index.html', {'persons': persons})
    elif path == 'add':
        bo = personBO()
        return render(request, 'add.html', {'bo': bo})

def edit(request,id):

    person = Person.objects.get(id=id)
    bo = personBO(
        initial={'id':id,'name': person.name, 'age': person.age}
    )
    return render(request, 'add.html', {'bo': bo})

def addAction(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    Person.objects.create(name=name, age=age)
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})


def deleteAction(request, id):
    Person.objects.filter(id=id).delete()
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})


def editAction(request,id):
    name1 = request.POST.get("name")
    age1 = request.POST.get("age")
    Person.objects.get(pk=id).update(name=name1,age=age1)
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})

def returnJSONAction(request):
    jsonObject=serializers.serialize('json',Person.objects.all())
    return HttpResponse(jsonObject,content_type='application/json')

