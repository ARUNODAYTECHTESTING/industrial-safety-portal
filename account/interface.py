from abc import ABC,abstractmethod
from typing import List
class IDepartment(ABC):

    @abstractmethod
    def get_all_departments(self) -> List:
        pass

    @abstractmethod
    def add_department(self,department: str):
        pass



class IUser(ABC):
    @abstractmethod
    def add_user(self):
        pass
    
    @abstractmethod
    def get_user_by_token_id(self,token_id: str):
        pass

    @abstractmethod
    def get_user_by_id(self,user_id: str):
        pass
    
class ITokenizer(ABC):
    @abstractmethod
    def generate_token(self):
        pass


class IGroup(ABC):

    @abstractmethod
    def get_user_type_level(self) -> List:
        pass

    @abstractmethod
    def get_user_role(self) -> str:
        pass