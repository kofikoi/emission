# import csv
# from django.core.management.base import BaseCommand
# from emissiondataapp.models import Emission, Country

# class Command(BaseCommand):
#     help = 'Loads data from a CSV file into the Emission model'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', type=str, help='Path to the CSV file')

#     def handle(self, *args, **options):
#         csv_file_path = options['csv_file']
#         with open(csv_file_path) as f:
#             reader = csv.reader(f)
#             next(reader) # skip header row
#             for row in reader:
#                 try:
#                     country_name, iso_alpha, year, total_emissions, coal, oil, gas_fuel_emissions, cement, flaring, other, per_capita = row
#                     country, created = Country.objects.get_or_create(name=country_name)
#                     emission = Emission(
#                         country=country,
#                         iso_alpha=iso_alpha,
#                         year=int(year),
#                         total_emissions=float(total_emissions),
#                         coal=float(coal),
#                         oil=float(oil),
#                         gas_fuel_emissions=float(gas_fuel_emissions),
#                         cement=float(cement),
#                         flaring=float(flaring),
#                         other=float(other),
#                         per_capita=float(per_capita),
#                     )
#                     emission.save()
#                 except ValueError:
#                     pass # skip row if not enough values to unpack
#         self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
import json
from django.core.management.base import BaseCommand
from emissiondataapp.models import Emission, Country

class Command(BaseCommand):
    help = 'Loads data from a JSON file into the Emission model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file_path = options['json_file']
        with open(json_file_path) as f:
            data = json.load(f)
            for row in data:
                try:
                    country_name = row['Country']
                    iso_alpha = row['ISO 3166-1 alpha-3']
                    year = row['Year']
                    total_emissions = row['Total']
                    coal = row['Coal']
                    oil = row['Oil']
                    gas_fuel_emissions = row['Gas']
                    cement = row['Cement']
                    flaring = row['Flaring']
                    other = row['Other']
                    per_capita = row['Per Capita']
                    country, created = Country.objects.get_or_create(name=country_name)
                    emission = Emission(
                        country=country,
                        iso_alpha=iso_alpha,
                        year=int(year),
                        total_emissions=float(total_emissions),
                        coal=float(coal),
                        oil=float(oil),
                        gas_fuel_emissions=float(gas_fuel_emissions),
                        cement=float(cement),
                        flaring=float(flaring),
                        other=float(other),
                        per_capita=float(per_capita),
                    )
                    emission.save()
                except ValueError:
                    pass # skip row if not enough values to unpack
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
