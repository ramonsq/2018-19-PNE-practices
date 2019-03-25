class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return str(len(self.strbases))

    def complement(self):
        comp_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
        translation = self.strbases.maketrans(comp_bases)
        strbases_comp = self.strbases.translate(translation)
        return str(Seq(strbases_comp))

    def reverse(self):
        strbases_rev = self.strbases[::-1]
        return str(Seq(strbases_rev))

    def count(self, base):
        n_base = self.strbases.count(base)
        return str(n_base)

    def perc(self, base):
        total_length = len(self.strbases)
        if total_length > 0:
            nbase = self.count(base)
            perc = str(round(100.0 * int(nbase) / total_length, 1))
        else:
            perc = 0

        return perc