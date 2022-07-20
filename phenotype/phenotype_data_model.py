from dataclasses import dataclass
from typing import Optional, Union

from phenotype.phenotypes_interface import Phenotypes


@dataclass
class PhenotypeConfig:
    phenotype_function: Phenotypes = Phenotypes.TEST
    expected_phenotype_value: Optional[Union[int, float]] = None
