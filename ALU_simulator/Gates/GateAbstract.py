from abc import ABC, abstractmethod


class GateAbstract(ABC):
    @abstractmethod
    def get_output(self) -> str:
        pass
    
    
    @abstractmethod
    def __validate_input(self):
        pass
    
    
    @abstractmethod
    def __execute(self):
        pass