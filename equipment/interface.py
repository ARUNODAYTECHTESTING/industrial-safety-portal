
import abc
from typing import List

class IPlant(abc.ABC):
    @abc.abstractmethod
    def get_all_plants(self) -> List:
        pass