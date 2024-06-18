import random
import os

from .models import Voter
class SamplingStrategy:
    def sample_voters(self):
        pass

    def sample_voters_tsv(self):
        voters = self.sample_voters()
        return "\n".join(["\t".join([str(v.id), v.gender, v.city, v.selection]) for v in voters])

class SimpleRandomSampling(SamplingStrategy):
    def sample_voters(self):
        return random.sample(list(Voter.objects.all()), 30)  # Example sample size of 10


    def sample_voters_tsv(self):
        # city1_voters.tsv dosyasının tam yolu
        file_path = os.path.join(self.BASE_DIR, 'city1_voters.tsv')
        
        # Dosyayı açıp içeriğini oku
        with open(file_path, 'r') as file:
            voters_data = file.readlines()

        # İçeriği düzenle
        formatted_data = []
        for line in voters_data:
            voter_info = line.strip().split('\t')
            # Voter nesneleri oluşturulacaksa burada oluşturulabilir
            formatted_data.append("\t".join(voter_info))

        # TSV formatında veriyi döndür
        return "\n".join(formatted_data)


class IntervalSampling(SamplingStrategy):
    def sample_voters(self):
        return Voter.objects.all()[::10]

    def sample_voters_tsv(self):
        voters = self.sample_voters()
        return "\n".join(["\t".join([str(v.id), v.gender, v.city, v.selection]) for v in voters])

class StratifiedSampling(SamplingStrategy):
    def sample_voters(self):
        city1_voters = list(Voter.objects.filter(city='City1'))
        city2_voters = list(Voter.objects.filter(city='City2'))
        city3_voters = list(Voter.objects.filter(city='City3'))

        selected_voters = []
        selected_voters.extend(random.sample(city1_voters, 10))
        selected_voters.extend(random.sample(city2_voters, 10))
        selected_voters.extend(random.sample(city3_voters, 10))

        return selected_voters

    def sample_voters_tsv(self):
        voters = self.sample_voters()
        return "\n".join(["\t".join([str(v.id), v.gender, v.city, v.selection]) for v in voters])

class SamplingContext:
    def __init__(self, strategy: SamplingStrategy):
        self.strategy = strategy

    def sample_voters(self):
        return self.strategy.sample_voters()

    def sample_voters_tsv(self):
        return self.strategy.sample_voters_tsv()
