from django.shortcuts import render, redirect
from .models import People

# Create your views here.
def home(request):
  peoples = People.objects.all()
  return render(request, 'index.html', {'peoples': peoples})

def save(request):
  name = request.POST.get('name')
  People.objects.create(name=name)
  peoples = People.objects.all()
  return render(request, 'index.html', {'peoples': peoples})

def edit(request, id):
  people = People.objects.get(id=id)
  return render(request, 'update.html', {'people': people})

def update(request, id):
  name = request.POST.get('name')
  people = People.objects.get(id=id)
  people.name = name
  people.save()

  return redirect(home)

def delete(request, id):
  people = People.objects.get(id=id)
  people.delete()
  return redirect(home)
