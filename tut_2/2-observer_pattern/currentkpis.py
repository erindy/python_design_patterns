from IObservers import AbsObserver
from kpis import KPIs

class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis: KPIs) -> None:
        # subscribe to kpi by attaching itself
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

    def display(self):
        print("Current apis")
        print(self.open_tickets, self.closed_tickets, self.new_tickets)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)




class ForecastKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis: KPIs) -> None:
        # subscribe to kpi by attaching itself
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

    def display(self):
        print("Forecast apis")
        print(self.open_tickets, self.closed_tickets, self.new_tickets)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)


if __name__=="__main__":
    kpis = KPIs()
    currentKPIs = CurrentKPIs(kpis)
    forecastKPIs = ForecastKPIs(kpis)
    kpis.set_kpis(35, 65,34)
    kpis.set_kpis(305, 965,394)
    kpis.set_kpis(315, 652,394)
    print('detaching...')
    kpis.detach(currentKPIs)
    kpis.set_kpis(1,3,4)