from typing import List

from genotype.genotype import Genotype
from phenotype.abstract_phenotype import AbstractPhenotype


class ChallengePhenotype(AbstractPhenotype):
    def __init__(self):
        super().__init__()

    @property
    def expected_value(self):
        pass

    def optimise_for_list_genotype(self, genotype: Genotype):
        # convert binary to decimal
        decimal_parameter = self.convert_binary_to_decimal(genotype.genotype)
        # evaluate phenotype
        phenotype_func = decimal_parameter ** 2 *(-1)
        return phenotype_func

    def optimise_for_string_genotype(self, genotype: Genotype):
        pass

    def convert_binary_to_decimal(self, number_in_binary: List[int]) -> int:

        # go through each element of list backwards
        # add
        power_of_2 = 0
        equivalent_int = 0

        for i in range(len(number_in_binary) - 1, -1,  -1):
            binary_component = number_in_binary[i] * (2 ** power_of_2)
            equivalent_int += binary_component

            power_of_2 += 1

        return equivalent_int

if __name__ == '__main__':
    test_phenotype = ChallengePhenotype()
    print(test_phenotype.convert_binary_to_decimal([0, 0, 1])) # 1
    print(test_phenotype.convert_binary_to_decimal([1, 0, 1])) # 1 + 4 = 5
    print(test_phenotype.convert_binary_to_decimal([1, 1, 1, 1])) # 1+2+4+8 =15
