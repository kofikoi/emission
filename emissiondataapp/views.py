from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from emissiondataapp.models import Emission, Country
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Country, Emission
from django.db.models import F


def index(request):
    # This is our landing page for the app
    return render(request, 'index.html')

def sign_up(request):
    #this allows the user create an account
    return render(request, 'signup.html')


class CountryListView(ListView):
    model = Emission
    template_name = 'country_list.html'
    context_object_name = 'emissions'
    paginate_by = 15 # Set the number of objects to be displayed per page

    def get_queryset(self):
        queryset = Emission.objects.annotate(
            country_name=F('country__name')
        ).values('country_id', 'country_name', 'total_emissions', 'year')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emissions'] = context['object_list']
        return context


class CountryDetailView(DetailView):
    model = Country
    template_name = 'country_detail.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.get_object()
        context['emissions'] = Emission.objects.filter(country=country)
        return context


