import os
import django
import random
from faker import Faker
import json

# Django projesini ayarlama
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'election_prediction.settings')
django.setup()

from election_simulator.models import Voter

fake = Faker()

# Şehir, cinsiyet ve seçim seçenekleri
CITIES = ['City1', 'City2', 'City3']
GENDER_CHOICES = ['Male', 'Female', 'Other']
SELECTION_CHOICES = ['A', 'B', 'C']

# Verileri oluşturmak için listeler
city1_data = []
city2_data = []
city3_data = []

def create_voter(city):
    age = random.randint(18, 90)
    name = fake.name()
    gender = random.choice(GENDER_CHOICES)
    selection = random.choice(SELECTION_CHOICES)

    voter = Voter.objects.create(city=city, age=age, name=name, gender=gender, selection=selection)
    
    # Veriyi uygun formata ekle
    if city == 'City1':
        city1_data.append(f"{voter.name}\t{voter.age}\t{voter.gender}\t{voter.selection}\n")
    elif city == 'City2':
        city2_data.append({
            'name': voter.name,
            'age': voter.age,
            'gender': voter.gender,
            'selection': voter.selection
        })
    elif city == 'City3':
        city3_data.append({
            'name': voter.name,
            'age': voter.age,
            'gender': voter.gender,
            'selection': voter.selection
        })

if __name__ == '__main__':
    # Her şehir için 100 veri oluştur
    for city in CITIES:
        for _ in range(100):
            create_voter(city)

    # City1 için TSV formatında veri yaz
    with open('city1_data.tsv', 'w') as tsvfile:
        tsvfile.write("name\tage\tgender\tselection\n")
        for row in city1_data:
            tsvfile.write(row)

    # City2 ve City3 için JSON formatında veri yaz
    with open('city2_data.json', 'w') as jsonfile:
        json.dump(city2_data, jsonfile, indent=4)

    with open('city3_data.json', 'w') as jsonfile:
        json.dump(city3_data, jsonfile, indent=4)

    print("Veriler başarıyla oluşturuldu ve dosyalara yazıldı.")
