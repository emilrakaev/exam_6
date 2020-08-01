from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import Guest
from webapp.forms import GuestForm


def index_view(request):
    data = Guest.objects.all()
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
