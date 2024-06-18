# generate_city1_tsv.py

import random
from faker import Faker

fake = Faker()

def generate_tsv(filename, num_records):
    with open(filename, 'w', encoding='utf-8') as file:
        # Write header
        file.write('city\tage\tname\tgender\tselection\n')
        
        for _ in range(num_records):
            city = 'City1'
            age = random.randint(18, 80)
            name = fake.name()
            gender = random.choice(['Male', 'Female', 'Other'])
            selection = random.choice(['A', 'B', 'C'])
            
            file.write(f'{city}\t{age}\t{name}\t{gender}\t{selection}\n')
    
    print(f'{num_records} records written to {filename}')

if __name__ == "__main__":
    generate_tsv('city1_voters.tsv', 100)
