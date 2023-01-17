from abc import abstractmethod, ABC

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Renderable(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

class Frame(ABC):

    @abstractmethod
    def display(self):
        pass
