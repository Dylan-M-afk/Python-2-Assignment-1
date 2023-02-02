from unittest import TestCase

from datetime import date
from employee import Employee

class TestEmployee(TestCase):
    def test_employee_init(self):
        e = Employee(first_name="John", last_name="Doe", salary=1000, date_of_birth=date(2000,1,24))
        self.assertEqual(e.name, "John Doe")

    def test_employee_annual_salary(self):
        e = Employee(first_name="John", last_name="Doe", salary=1000, date_of_birth=date(2000,1,24))
        self.assertEqual(e.annual_salary, 12000)

    def test_employee_pay_raise(self):
        e = Employee(first_name="John", last_name="Doe", salary=1000, date_of_birth=date(2000,1,24))
        e.raise_salary(raise_percent=10)
        self.assertEqual(e.annual_salary, 1100*12)

    def test_emp_id(self):
        e1 = Employee(first_name="John", last_name="Doe", salary=1000, date_of_birth=date(2000,1,24))
        e2 = Employee(first_name="Johny", last_name="Doe", salary=1000, date_of_birth=date(2000,1,24))
        self.assertEqual(e1.employee_id, 'E0001')
        self.assertEqual(e2.employee_id, 'E0002')

    def test_property_age(self):
        e1 = Employee(first_name="John", last_name="Doe", salary=1000, date_of_birth=date(2000, 1, 24))
        self.assertEqual(e1.age, 23)