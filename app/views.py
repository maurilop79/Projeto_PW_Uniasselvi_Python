from django.shortcuts import render, redirect
from app.forms import JogosForm
from app.models import Jogos
# Create your views here.
def home(request):
    data = {}
    data['db'] = Jogos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data ['form'] = JogosForm()
    return render(request, 'form.html', data)

def create(request):
    form = JogosForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Jogos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Jogos.objects.get(pk=pk)
    data['form'] = JogosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Jogos.objects.get(pk=pk)
    form = JogosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Jogos.objects.get(pk=pk)
    db.delete()
    return redirect('home')



