
import abc
from typing import List

class IPlant(abc.ABC):
    @abc.abstractmethod
    def get_all_plants(self) -> List:
        pass


class ISchedule(abc.ABC):
    @abc.abstractmethod
    def get_schedule_by_user(self,user) -> List:
        pass

class IEquipment(abc.ABC):
    @abc.abstractmethod
    def get_equipment_by_id(self,id) -> List:
        pass