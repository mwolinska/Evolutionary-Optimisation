from typing import Tuple, Optional, Union

from matplotlib import pyplot as plt

from evolution.population import Population
from fitness_score.fitness_score import FitnessScore
from genotype.genotype_data_model import GenotypeProperties, GenotypeKey, Gene
from phenotype.phenotype_data_model import PhenotypeConfig
from phenotype.phenotypes_interface import Phenotypes


class Evolution:
    def __init__(
        self,
        n_individuals: int,
        n_generations: int,
        genotype_properties: GenotypeProperties,
        phenotype_config: PhenotypeConfig,
        crossover: bool = False
    ):
        """Initialises Evolution class.

        The evolution class performs evolutionary optimisation of a function (a phenotype).
        It contains a population of individuals that are evaluated at every iteration (generation)
        of the algorithm.

        Args:
            n_individuals: number of individuals in the desired population.
            n_generations: number of iterations of the algorithm.
            genotype_properties: all properties required to build an individual.
                As defined by the GenotypeProperties class.
            phenotype_config: parameters needed to create / act on AbstractPhenotype instance.
            crossover: whether crossover should happen when updating the population.
        """
        self.genotype_properties = genotype_properties

        self.population = Population(n_individuals,
                                     self.genotype_properties,
                                     phenotype_config=phenotype_config,
                                     crossover=crossover)
        self.epochs = n_generations
        self.fitness_over_time = []

    def evolve(self):
        """Performs evolutionary optimisation.

        This function performs the evolutionary optimisation. Over n_generations it evaluates the population,
        updates the population (with crossover and/ or mutation as initialised). It then record the
        best fitness score at each generation. Once optimisation is complete it plots the performance over time.
        """
        for n in range(self.epochs):
            self.evaluate_population()
            self.population.update_population()
            self.record_performance()

        print(f"The value of the best individual is {self.population.best_individual.genotype.genotype}")
        self.plot_performance()

    def evaluate_population(self):
        """Calculates fitness scores for each individual in population.

        For each individual in the population calculates the fitness score and stores the best individual
        in the population.best_individual attribute.
        """
        for individual in self.population.all_individuals:
            fitness_score = FitnessScore(individual).calculate_score()

            individual.fitness_score = fitness_score
            if self.population.best_individual.fitness_score is None or \
                    fitness_score > self.population.best_individual.fitness_score:
                self.population.best_individual = individual

    def record_performance(self):
        """Record fitness function value of the current best individual."""
        self.fitness_over_time.append(self.population.best_individual.fitness_score)

    def plot_performance(self):
        """Plots score of the best individual at each generation."""
        x_axis = list(range(0, len(self.fitness_over_time)))
        plt.plot(x_axis, self.fitness_over_time)
        plt.title('Algorithm Performance Over Time')
        plt.xlabel('Epoch')
        plt.ylabel('Fitness score')
        plt.show()
