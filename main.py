import math

from evolution.evolution import Evolution

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

    test_evolution = Evolution(
        n_individuals=100, # increase n_indiv to magnitude 10-100
        n_generations=20, # normally > 100
        genotype_properties=genotype_properties,
        phenotype_config=phenotype_config,
        crossover=True
    )

    test_evolution.evolve()


if __name__ == '__main__':
    run_evolution()
