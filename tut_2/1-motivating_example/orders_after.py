from abc import ABC, abstractmethod


class Order:
    pass


class IStrategy(ABC):

    @abstractmethod
    def calculate_cost(self, order: Order) -> int:
        pass


class UPS(IStrategy):
    def calculate_cost(self, order: Order):
        return 4.00


class Fedex(IStrategy):
    def calculate_cost(self, order: Order):
        return 5.00


class Postal(IStrategy):
    def calculate_cost(self, order: Order):
        return 6.00


class Shipping:
    def __init__(self, strategy: IStrategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        self._strategy.calculate_cost(order)