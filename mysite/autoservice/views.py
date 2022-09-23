from django.shortcuts import render, get_object_or_404
from .models import Automobilis, Paslauga, Uzsakymas
from django.views import generic
from django.core.paginator import Paginator


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
    paginator = Paginator(Automobilis.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_auto = paginator.get_page(page_number)
    kontext = {
        'automobiliai': paged_auto
    }

    return render(request, 'automobiliai.html', context=kontext)


def paslaugos(request):
    pasl = Paslauga.objects.all()
    kontext = {
        'paslaugos': pasl
    }

    return render(request, 'paslaugos.html', context=kontext)


def automobilis(request, automobilis_id):
    vienas_auto = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, 'automobilis.html', {'automobilis': vienas_auto})


class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = 'uzsakymas_list.html'


class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas_detail.html'
