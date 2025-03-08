
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
    @abc.abstractmethod
    def get_schedule_by_user_list(self, user_list) -> List:
        pass
    @abc.abstractmethod
    def get_schedule_assigned_by(self, assigner) -> List:
        pass
    @abc.abstractmethod
    def get_schedule_by_equipment(self, equipment_id,user_id) -> object:
        pass

class IEquipment(abc.ABC):
    @abc.abstractmethod
    def get_equipment_by_id(self,id) -> List:
        pass
    @abc.abstractmethod
    def get_object(self,id)->object:
        pass


class ICheckPoint(abc.ABC):
    @abc.abstractmethod
    def get_object(self, id) -> object:
        pass