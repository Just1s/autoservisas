from django.shortcuts import render, get_object_or_404
from .models import Automobilis, Paslauga, Uzsakymas
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    auto_kiekis = Automobilis.objects.count()
    paslaugu_kiekis = Paslauga.objects.count()
    uzsakymu_kiekis = Uzsakymas.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    kontext = {'auto_kiekis': auto_kiekis,
               'paslaugu_kiekis': paslaugu_kiekis,
               'uzsakymu_kiekis': uzsakymu_kiekis,
               'num_visits': num_visits
               }

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


def search(request):
    query_text = request.GET.get('query')
    search_results = Automobilis.objects.filter(Q(klientas__icontains=query_text) |
                                                Q(vin__icontains=query_text) |
                                                Q(valst_nr__icontains=query_text) |
                                                Q(auto_modelis_id__marke__icontains=query_text) |
                                                Q(auto_modelis_id__modelis__icontains=query_text))
    return render(request, 'search.html', {'automobiliai': search_results, 'querytxt': query_text})


class OrdersByUserListView(LoginRequiredMixin, generic.ListView):
    model = Uzsakymas  # konteksto kint i sablona uzsakymas_list
    template_name = 'user_orders.html'
    paginate_by = 10

    def get_queryset(self):
        return Uzsakymas.objects.filter(vartotojas=self.request.user).filter(status__exact='a').order_by('atsiimti_iki')
