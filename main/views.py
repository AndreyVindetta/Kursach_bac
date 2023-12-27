from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm
from django.views.generic import DetailView, UpdateView, DeleteView
#в зависсимости от того или иного url адреса, показываем тот или иной html шаблон


def index(request):
    clients = Client.objects.order_by('id')  # [:1]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'clients': clients})


class ClientDetailView(DetailView):
    model = Client
    template_name = 'main/details_view.html'
    context_object_name = 'client'


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'main/create.html'
    form_class = ClientForm
    success_url = reverse_lazy('home')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('home')
    template_name = 'main/client_delete.html'


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ClientForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

