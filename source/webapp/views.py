from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import Guest
from webapp.forms import GuestForm


def index_view(request):
    data = Guest.objects.all().filter(status='active')
    return render(request, 'index.html', context={
        'guests': data
    })


def guest_create_view(request):
    if request.method == 'GET':
        return render(request, 'guest_create.html', context={
            'form': GuestForm()
        })
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest = Guest.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'guest_create.html', context={
                'form': form
            })


def guest_update_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text
        })
        return render(request, 'guest_update.html', context={
            'form': form,
            'guest': guest
        })
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'guest_update.html', context={
                'guest': guest,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guest_delete_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guest_search_view(request):
    query=request.GET.get("searching")
    data = Guest.objects.filter(name__icontains=query)
    return render(request, 'guest_search.html', context={
        'guests': data
    })

