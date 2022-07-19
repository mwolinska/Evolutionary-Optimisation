from abc import ABC, abstractmethod

from genotype.genotype import Genotype


class AbstractPhenotype(ABC):

    def __init__(self):
        self._expected_value = None

    @abstractmethod
    def function_to_optimise(self, genotype: Genotype):
        pass

    @abstractmethod
    def optimise_for_string_genotype(self, genotype: Genotype):
        pass

    @property
    @abstractmethod
    def expected_value(self):
        pass
        # return self._expected_value

    @expected_value.setter
    @abstractmethod
    def expected_value(self, exp_value):
        pass
        # self._expected_value = exp_value
