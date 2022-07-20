import math

from evolution.evolution import Evolution, EvolutionProperties

from genotype.genotype_data_model import GenotypeKey, GenotypeProperties, Gene
from phenotype.phenotype_data_model import PhenotypeConfig
from phenotype.phenotypes_interface import Phenotypes


def run_evolution():
    genotype_properties = GenotypeProperties(genotype_key=GenotypeKey(list),
                                             type_of_gene=Gene(int),
                                             n_genes=32,
                                             value_range=(0, 1),
                                             mutation_probability=0.1,
                                             )

    phenotype_config = PhenotypeConfig(phenotype_function=Phenotypes.CHALLENGE,
                                       expected_phenotype_value=None,
                                       )

    evolution_properties = EvolutionProperties(n_individuals=100,
                                               n_generations=20,
                                               genotype_properties=genotype_properties,
                                               phenotype_config=phenotype_config,
                                               crossover=True,
                                               crossover_percentage=0.5,
                                               elitism=0.1,
                                               )

    test_evolution = Evolution(evolution_properties)

    test_evolution.evolve()


if __name__ == '__main__':
    run_evolution()

# problem:
# currently optimising f(x) which is -x^2
# now: still optimise for x but f(x_1, x_2, x_3, ... x_n)
# x_1 .. x_2 are bits that make up x
# x_1 = x_2 is the binary value of x
#  001 = 2^0 * 1 + 0 + 0
# the search space is not x, but the binary value of x


# REQ STEPS (not in order)
# write function to convert binary to decimal
# set gene type to int (double check)
#


# genotype_key=list,
# type_of_gene=bin,
# n_genes=32, # set back to 32 before final test
# # gene_value_range=(-math.exp(40), math.exp(40)), # defaults -infinity, + infinity
# mutation_probability=0.3,
# phenotype="challenge", # this should be type AbstractPhenotype
# expected_phenotype_value=None,


# class EA():
#     def __init__(self, phenotype: Phenotype):
#         self.phenotype = phenotype
#
#     def run(self):
#         pass
#     def random_pop(self):
#         self.phenotype.random()
#
# class Genotype:
#
#     def random(self):
#         return 1
#
# class Phenotype:
#     def __init__(self, genotype: Genotype):
#         self.genotype = genotype
#
#     def random(self):
#         self.genotype.random()
#
# class Fitness:
#     pass
