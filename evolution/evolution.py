from dataclasses import dataclass
from typing import Tuple, Optional, Union

from matplotlib import pyplot as plt

from evolution.population import Population
from fitness_score.fitness_score import FitnessScore
from genotype.genotype_data_model import GenotypeProperties
from phenotype.phenotype_data_model import PhenotypeConfig

@dataclass
class EvolutionProperties:
    n_individuals: int = 100
    n_generations: int = 20
    genotype_properties: GenotypeProperties = GenotypeProperties()
    phenotype_config: PhenotypeConfig = PhenotypeConfig()
    crossover: bool = False
    crossover_percentage: float = 0.5
    elitism: float = 0.1

class Evolution:
    def __init__(
        self,
        evolution_properties: EvolutionProperties
    ):
        """Initialises Evolution class.

        The evolution class performs evolutionary optimisation of a function (a phenotype).
        It contains a population of individuals that are evaluated at every iteration (generation)
        of the algorithm.

        Args:
            evolution_properties: contains all required information to run an optimisation.
        """
        self.genotype_properties = evolution_properties.genotype_properties

        self.population = Population(evolution_properties.n_individuals,
                                     self.genotype_properties,
                                     phenotype_config=evolution_properties.phenotype_config,
                                     crossover=evolution_properties.crossover)
        self.epochs = evolution_properties.n_generations
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
