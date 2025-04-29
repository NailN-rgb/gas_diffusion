from ABC import ABC, abstractmethod

class BaseAssembler():
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def assemble_element(self):
        pass