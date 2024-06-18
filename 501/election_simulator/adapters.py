# adapters.py

class TSVAdapter:
    def __init__(self, voters):
        self.voters = voters

    def get_tsv(self):
        return "\n".join(["\t".join([str(v.id), v.city,  str(v.age), v.gender, v.selection]) for v in self.voters])
