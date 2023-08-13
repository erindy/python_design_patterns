from abc import ABC, abstractmethod

class AbsObserver(ABC):

    @abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class AbsSubject(ABC):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from ABSObserver')
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)