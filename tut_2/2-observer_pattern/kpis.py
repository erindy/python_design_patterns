from IObservers import AbsObserver, AbsSubject

class KPIs(AbsSubject):
    _open_ticket = -1
    _closed_ticket = -1
    _new_ticket = -1


    @property
    def open_tickets(self):
        return self._open_ticket

    @property
    def closed_tickets(self):
        return self._closed_ticket

    @property
    def new_tickets(self):
        return self._new_ticket

    def set_kpis(self, open_tickets, closed_ticket, new_ticket):
        self._open_ticket = open_tickets
        self._closed_ticket = closed_ticket
        self._new_ticket = new_ticket
        self.notify()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()