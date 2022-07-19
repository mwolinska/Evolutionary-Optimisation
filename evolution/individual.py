from genotype.genotype import Genotype
from genotype.genotype_data_model import GenotypeProperties, GenotypeKey
from phenotype.phenotypes_interface import Phenotypes


class Individual:
    def __init__(self, genotype_properties: GenotypeProperties, phenotype: Phenotypes):
        """An object containing all information of one instance being evaluated.

        An individual is effectively an instance being evaluated during the evolution. An individual contains
        a genotype and a fitness score (updated upon evaluation during Evolution).

        Args:
            genotype_properties: all genotype properties as required for an individual.
        """
        self.genotype = Genotype(genotype_properties)
        self.phenotype = phenotype
        self.phenotype_value = self.get_phenotype_value()
        self.fitness_score = None

    @classmethod
    def from_genotype(cls, genotype_properties: GenotypeProperties, new_genotype):
        """Creates an individual from a genotype.

        An individual is created, but instead of a random set of genes the new_all_genes argument
        is used to populate the individual.all_genes attribute.

            genotype_properties: all genotype properties as required for an individual.
            new_all_genes: an instance of all_genes in alignment with the GenotypeKey defined by genotype_properties.
        Returns:
            An Individual object with the genotype properties passed in the function except for
                individual.all_genes which contain the new_all_genes information.
        """
        # TODO how to deal with type of new_genotype.
        new_individual = cls(genotype_properties)
        new_individual.genotype.genotype = new_genotype
        return new_individual

    def mutation(self):
        """Performs mutation of the individual.

        The genotype attribute is updated through a mutation in line with the function definition within the
        Genotype class.
        """
        new_genotype = self.genotype.mutate()
        self.genotype.genotype = new_genotype
        self.phenotype_value = self.get_phenotype_value()

    def get_phenotype_value(self):
        phenotype_instance = Phenotypes.get_phenotype(self.phenotype)
        phenotype_value = None

        if self.genotype.genotype_key == GenotypeKey.LIST:
            phenotype_value = phenotype_instance.optimise_for_list_genotype(self.genotype)
        elif self.genotype.genotype_key == GenotypeKey.STRING:
            phenotype_value = phenotype_instance.optimise_for_string_genotype(self.genotype)

        return phenotype_value


def get_score_for_sorting(individual: Individual):
    """Key for sort function used in Population object.

    Provides a key for sorting individuals using python's sort function used by the update_population function
    within the Population object.

    Args:
        individual: an Individual instance.
    Returns:
        Float equal to an individual's fitness score.
    """
    return individual.fitness_score
