from abc import ABC, abstractmethod


class AdderAbstract(ABC):
    @abstractmethod
    def get_s(self) -> str:
        pass
    
    
    @abstractmethod
    def get_carry_out(self) -> str:
        pass
    
    
    @abstractmethod
    def __validate_input(self):
        pass
    
    
    @abstractmethod
    def __execute(self):
        pass


class AdderOverflowAbstract(ABC):
    @abstractmethod
    def get_s(self) -> str:
        pass
    
    
    @abstractmethod
    def get_overflow(self) -> str:
        pass
    
    
    @abstractmethod
    def __validate_input(self):
        pass
    
    
    @abstractmethod
    def __execute(self):
        pass