"""
non Pythonic way
Dangling reference (Memory leak)
"""

from observers import AbsObserver
from subjects import AbsSubject


class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print('Current open tickets: {}'.format(self.open_tickets))
        print('New tickets in last hour: {}'.format(self.closed_tickets))
        print('Tickets closed in last hour: {}'.format(self.new_tickets))
        print('*****\n')


class ForecastKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print('Forecast open tickets: {}'.format(self.open_tickets))
        print('New tickets expected in next hour: {}'.format(self.closed_tickets))
        print('Tickets expected to be closed in next hour: {}'.format(self.new_tickets))
        print('*****\n')


class KPIs(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()


if __name__ == '__main__':
    # Report on current KPI values
    kpis = KPIs()
    currentKPIs = CurrentKPIs(kpis)
    forecastKPIs = ForecastKPIs(kpis)
    kpis.set_kpis(25, 10, 5)
    kpis.set_kpis(100, 50, 30)
    kpis.set_kpis(50, 10, 20)

    print('\n***Detaching the currentKPIs observer.***\n\n')
    kpis.detach(currentKPIs)
    kpis.set_kpis(150, 110, 120)
