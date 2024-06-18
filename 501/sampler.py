import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "election_prediction.settings")
django.setup()

from election_simulator.models import Voter
import random

def populate_data():
    cities = ['City1', 'City2', 'City3']
    genders = ['Male', 'Female', 'Other']
    selections = ['A', 'B', 'C']

    for city in cities:
        for _ in range(100):
            age = random.randint(18, 80)
            name = f"{random.choice(['John', 'Jane', 'Alice', 'Bob'])} {random.choice(['Doe', 'Smith', 'Johnson'])}"
            gender = random.choice(genders)
            selection = random.choice(selections)
            Voter.objects.create(city=city, age=age, name=name, gender=gender, selection=selection)

if __name__ == '__main__':
    populate_data()
