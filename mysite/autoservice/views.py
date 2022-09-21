from django.shortcuts import render
from django.http import HttpResponse
from .models import Automobilis, Paslauga, Uzsakymas


# Create your views here.
def index(request):
    auto_kiekis = Automobilis.objects.count()
    paslaugu_kiekis = Paslauga.objects.count()
    uzsakymu_kiekis = Uzsakymas.objects.count()
    kontext = {'auto_kiekis': auto_kiekis,
               'paslaugu_kiekis': paslaugu_kiekis,
               'uzsakymu_kiekis': uzsakymu_kiekis}

    return render(request, 'index.html', context=kontext)


def automobiliai(request):
    auto = Automobilis.objects.all()
    kontext = {
        'automobiliai': auto
    }

    return render(request, 'automobiliai.html', context=kontext)


def paslaugos(request):
    pasl = Paslauga.objects.all()
    kontext = {
        'paslaugos': pasl
    }

    return render(request, 'paslaugos.html', context=kontext)
