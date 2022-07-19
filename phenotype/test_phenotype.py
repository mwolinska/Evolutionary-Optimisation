from genotype.genotype import Genotype
from phenotype.abstract_phenotype import AbstractPhenotype


class TestPhenotype(AbstractPhenotype):
    def __init__(self):
        super().__init__()

    @property
    def expected_value(self):
        return self._expected_value

    @expected_value.setter
    def expected_value(self, value):
        self._expected_value = value

    def optimise_for_list_genotype(self, genotype: Genotype):
        phenotype_value = genotype.genotype[0] ** 2 * (-1)
        return phenotype_value

    def optimise_for_string_genotype(self, genotype: Genotype):
        pass

    # def function_to_optimise(self, genotype: List[int]):
    #     y = genotype[0] ** 2 * (-1)
    #     # x = x[0]
    #     # y = -1 * x * (x - 1) * (x - 2) * (x - 3) * (x - 4)
    #     return y

if __name__ == '__main__':
    inst = TestPhenotype()
    TestPhenotype.expected_value = 6
    print()
