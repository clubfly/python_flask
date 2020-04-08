import abc

class ServiceTemplate (abc.ABC):

    @abc.abstractmethod
    def run(self) :
        return NotImplemented
