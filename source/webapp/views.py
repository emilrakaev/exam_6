from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import Guest
# from webapp.forms import GuestForm


def index_view(request):
    data = Guest.objects.all()
    return render(request, 'index.html', context={
        'guests': data
    })
