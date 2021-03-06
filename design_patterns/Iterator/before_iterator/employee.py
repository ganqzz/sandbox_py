class Employee(object):
    def __init__(self, empid, name, hiredate):
        self.empid = empid
        self.name = name
        self.hiredate = hiredate


class Employees(object):
    _employees = {}
    _headcount = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def get_employee(self, i):
        return self._employees[i]

    @property
    def headcount(self):
        return self._headcount
