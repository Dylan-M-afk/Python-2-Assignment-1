import datetime


class Employee(object):
    """A class representing an employee 

    Attributes:
        first_name : string, employee's first name
        last_name : string, employee's last name
        employee_id: string, employee's id number in format (E0001)
        salary: float, employee's salary, can be increased with raise_salary() method
        date_of_birth: Date, employee's DOB in datetime format

    @Properties:
        employee_id: getter
        annual_salary: returns yearly salary
        name: returns name in first_name last_name format
        age: calculates and returns age of Employee        

    Methods:
        raise_salary(raise_percent):  
            given a raise percent, increases employee's salary by that amount
        
    """
    employee_id_counter = 1

    def __init__(self, first_name, last_name, salary, date_of_birth) -> None:
        """constructs employee object's attributes

        Args:
            first_name (str): employee's first name
            last_name (str): employee's last name
            salary (float): employee's salary
            date_of_birth (Date): DOB of employee in datetime format
        """
        assert isinstance(first_name, str), 'first_name must be of type str'
        assert isinstance(last_name, str), 'last_name must be of type str'
        assert isinstance(date_of_birth, datetime.date), 'date_of_birth must be of type datetime.date'
        # The test cases provide an int but the assignment pdf says only allow float?
        # allowing both for now but can easily be changed
        assert type(salary) in [int,float]
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employee_id = 'E' + str(Employee.employee_id_counter).zfill(4)
        self.__salary = salary
        self.__date_of_birth = date_of_birth
        Employee.employee_id_counter += 1

    @property
    def employee_id(self):
        """getter property for employee_id

        Returns:
            str: employee_id. ex:(E0001)
        """
        return self.__employee_id

    @property
    def annual_salary(self):
        """calculates the annual salary of an employee

        Returns:
            float: employees salary * 12
        """
        return 12 * self.__salary

    @property
    def name(self):
        """property for employee's full name

        Returns:
            string: concatenated first and last name
        """
        return f'{self.__first_name} {self.__last_name}'

    @property
    def age(self):
        """calculates the current age of an employee using the current date and their birthday

        Returns:
            int: calculated age of employee
        """
        today = datetime.date.today()
        # If the current month is less than DOB month than there has been no birthday this year
        if today.month < self.__date_of_birth.month:
            return today.year - self.__date_of_birth.year - 1
        # If the birthday month has past we know they have had a birthday
        elif today.month > self.__date_of_birth.month:
            return today.year - self.__date_of_birth.year
        # If it is the birthday month check if the birthday has happened yet
        elif today.month == self.__date_of_birth.month:
            # If Birthday has happened
            if today.day < self.__date_of_birth.day:
                return today.year - self.__date_of_birth.year - 1
            # If no birthday has happened
            return today.year - self.__date_of_birth.year

    def raise_salary(self, raise_percent):
        """increase employee's salary by a given percent

        Args:
            raise_percent (int,float): the percent value to increase employee's salary by.
            ex 10 will raise salary by 10%
        """
        assert raise_percent > 0, 'raise_percent must be greater than 0'
        self.__salary += (self.__salary * (raise_percent / 100))


if __name__ == '__main__':
    while True:
        print()
        print('~~~Employee Testing~~~')
        print('1: create a Employee object')
        print('2: print employee id')
        print('3: print annual salary')
        print('4: print full name')
        print('5: print age')
        print('6: raise salary by %')
        print('0: exit')
        print()
        user_choice = input('Enter your choice > ')
        match user_choice:
            case '1':
                while True:
                    try:
                        user_fname = input('Enter first name: ')
                        user_lname = input('Enter last name: ')
                        user_salary = float(input('Enter salary: '))
                        user_day = int(input('Enter day for date of birth (1-31): '))
                        user_month = int(input('Enter month for date of birth (1-12): '))
                        user_year = int(input('Enter year for date of birth: '))
                        user_dob = datetime.date(day=user_day,month=user_month,year=user_year)
                        user_object_1 = Employee(first_name=user_fname,last_name=user_lname,salary=user_salary,date_of_birth=user_dob )
                    except ValueError:
                        print('Please enter a number')
                    except TypeError as te:
                        print(te)
                    except AssertionError as ae:
                        print(ae)
                    except Exception as e:
                        print(e)
                    else:
                        break
            case '2':
                try:
                    print(user_object_1.employee_id)
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '3':
                try:
                    print(user_object_1.annual_salary)
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '4':
                try:
                    print(user_object_1.name)
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '5':
                try:
                    print(user_object_1.age)
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '6':
                try:
                    to_raise_by = int(input('Please enter the raise amount ex:(10 will raise by 10%): '))
                    user_object_1.raise_salary(to_raise_by)
                except NameError:
                    print('You must create that object first!')
                except AssertionError as ae:
                    print(ae)
                except ValueError as ve:
                    print('Please enter an int')
            case '0':
                exit()
