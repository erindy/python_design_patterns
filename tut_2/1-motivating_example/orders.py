from enum import Enum


class Order:
    def __init__(self, shipper):
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shipper


class Shipper(Enum):
    fedex = 1
    ups = 2
    postal = 3


class ShippingCost:
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError(f'Invalid shipper {order.shipper}')

    def _fedex_cost(self, order):
        return 3.00

    def _ups_cost(self, order):
        return 4.00

    def _postal_cost(self, order):
        return 5.00


if __name__=="__main__":
    order = Order(Shipper.fedex)
    cost_calculator = ShippingCost()
    cost = cost_calculator.shipping_cost(order)
    assert cost == 3.0

    