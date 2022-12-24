from django.shortcuts import render, redirect
from .models import Task, About, Contact
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    abouts = About.objects.all()
    return render(request, 'main/about.html', {'title': 'Страницо о нас', 'abouts': abouts})


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', {'title': 'Контакты', 'contacts': contacts})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была не верной!"
    form = TaskForm
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)
