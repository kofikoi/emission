from django.test import TestCase, Client
from django.urls import reverse
from emissiondataapp.models import Emission, Country

class CountryListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.country = Country.objects.create(name='Nigeria')
        self.emission1 = Emission.objects.create(country=self.country, year=2020, total_emissions=2000)
        self.emission2 = Emission.objects.create(country=self.country, year=2021, total_emissions=2500)

    def test_country_list_view(self):
        response = self.client.get(reverse('country_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'country_list.html')
        self.assertContains(response, 'Nigeria')
        self.assertContains(response, '2000')
        self.assertContains(response, '2500')
        self.assertQuerysetEqual(
            response.context['emissions'], 
            ['<Emission: Emission object (1)>', '<Emission: Emission object (2)>']
        )
        
class CountryDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.country = Country.objects.create(name='Nigeria')
        self.emission1 = Emission.objects.create(country=self.country, year=2020, total_emissions=2000)
        self.emission2 = Emission.objects.create(country=self.country, year=2021, total_emissions=2500)

    def test_country_detail_view(self):
        url = reverse('country_detail', args=[self.country.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'country_detail.html')
        self.assertContains(response, 'Nigeria')
        self.assertContains(response, '2000')
        self.assertContains(response, '2500')
        self.assertQuerysetEqual(
            response.context['emissions'], 
            ['<Emission: Emission object (1)>', '<Emission: Emission object (2)>']
        )
