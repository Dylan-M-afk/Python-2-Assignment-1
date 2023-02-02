class Date(object):
    """A class to represent a date dd/mm/yyyy

    Attributes:
            day (int): Value representing the day of the month 1-31
            month (int): Value representing the month of the year 1-12
            year (int): Value representing the year 

    @Properties:
        day: setter and getter
        month: setter and getter
        year: setter and getter
        is_leap_year: Returns true or false if the provided year is a leap year
        is_valid_date: Returns True or False if a date is valid ex:(30/02/2022 returns False)
        next_day: Returns the following day ex (01/11/2022 returns 02/11/2022)
        
    """

    def __init__(self, day: int, month: int, year: int) -> None:
        """constructs all necessary attributes for the Date object

        Args:
            day (int): Value representing the day of the month 1-31
            month (int): Value representing the month of the year 1-12
            year (int): Value representing the year 

        Raises:
            TypeError: year cannot be a bool
            TypeError: month cannot be a bool
            TypeError: day cannot be a bool
            TypeError: day must be an int
            TypeError: month must be an int
            TypeError: year must be an int
            ValueError: day must be greater than 0
            ValueError: day must be less than 32
            ValueError: month must be greater than 0
            ValueError: month must be less than 13
        """

        # bool is a subclass of int? thus causes errors with comparing type with isinstance, have to use
        # if type(value) == bool: to avoid subclasses
        if type(year) == bool:
            raise TypeError('value cannot be a bool')
        if type(month) == bool:
            raise TypeError('value cannot be a bool')
        if type(day) == bool:
            raise TypeError('value cannot be a bool')
        if not isinstance(day, int):
            raise TypeError('day must be an int')
        if not isinstance(month, int):
            raise TypeError('month must be an int')
        if not isinstance(year, int):
            raise TypeError('year must be an int')
        if 0 >= day:
            raise ValueError('day must be greater than 0')
        if day >= 32:
            raise ValueError('Day must be less than 32')
        if 0 >= month:
            raise ValueError('month must be grater than 0')
        if month >= 13:
            raise ValueError('month must be less than 13')
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        return f"{str(self.day).zfill(2)}/{str(self.month).zfill(2)}/{str(self.year).zfill(4)}"

    @property
    def day(self):
        """getter property for day

        Returns:
            int: private day value
        """
        return self.__day

    @property
    def month(self):
        """getter property for month

        Returns:
            int: private month value
        """
        return self.__month

    @property
    def year(self):
        """getter property for year

        Returns:
            int: private year value
        """
        return self.__year

    @day.setter
    def day(self, new_day):
        """setter property for day

        Args:
            new_day (int): a value to set the private day value to

        Raises:
            AssertionError: 'New day must be an int'
        """
        assert isinstance(new_day,int), 'New day must be an int'
        self.__day = new_day

    @month.setter
    def month(self, new_month):
        """setter property for month

        Args:
            new_month (int): a value to set the private month value to

        Raises:
            AssertionError: 'New month must be an int'
        """
        assert isinstance(new_month, int), 'New month must be an int'
        self.__month = new_month

    @year.setter
    def year(self, new_year):
        """setter property for year

        Args:
            new_year (int): a value to set the private month value to

        Raises:
            AssertionError: 'New year must be an int'
        """
        assert isinstance(new_year, int), 'New year must be an int'
        self.__year = new_year

    @property
    def is_leap_year(self):
        """checks if the year value of the object is a leap year or not

        Returns:
            bool: True or False if the year is a leap year
        """
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    @property
    def is_valid_date(self):
        """checks if the date object is a valid date

        Returns:
            bool: True or False if the date is valid. ex: True:(25/10/2022) False:(31/02/2022)
        """
        match self.month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if self.day > 31:
                    return False
                return True
            case 4 | 6 | 9 | 11:
                if self.day > 30:
                    return False
                return True
            case 2:
                if self.day > 29:
                    return False
                if self.day == 29:
                    if self.is_leap_year:
                        return True
                    return False
                return True
            case _:
                return False

    @property
    def next_day(self):
        """calculates and returns the following day as a Date object

        Returns:
            Date: following day. ex: (31/12/2000 returns 01/01/2001)
        """
        next_day = Date(self.day, self.month, self.year)
        match self.month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if self.month == 12 and self.day == 31:
                    next_day.year += 1
                    next_day.month = 1
                    next_day.day = 1
                elif self.day == 31:
                    next_day.month += 1
                    next_day.day = 1
                else:
                    next_day.day += 1
            case 4 | 6 | 9 | 11:
                if self.day == 30:
                    next_day.month += 1
                    next_day.day = 1
                else:
                    next_day.day += 1
            case 2:
                if self.is_leap_year:
                    if self.day >= 29:
                        next_day.day = 1
                        next_day.month += 1
                    else:
                        next_day.day += 1
                elif self.day == 28:
                    next_day.day = 1
                    next_day.month += 1
                else:
                    next_day.day += 1
        return next_day


if __name__ == '__main__':
    while True:
        print()
        print('~~~Date Testing~~~')
        print('1: create a Date object')
        print('2: print Date object ')
        print('3: Check if Date is a leap year')
        print('4: Check if Date is a valid date')
        print('5: Print next day ')
        print('0: exit')
        print()
        user_choice = input('Enter your choice > ')
        match user_choice:
            case '1':
                while True:
                    try:
                        user_day = int(input('Enter the day (1-31): '))
                        user_month = int(input('Enter the month (1-12): '))
                        user_year = int(input('Enter the year: '))
                        user_object_1 = Date(day=user_day,month=user_month,year=user_year)
                    except ValueError:
                        print('Please enter a float')
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
                    print(user_object_1)
                except NameError:
                    print('Please create the object first!')
                except Exception as e:
                    print(e)
            case '3':
                try:
                    if user_object_1.is_leap_year:
                        print('It is a leap year!')
                    else:
                        print('It is not a leap year')
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '4':
                try:
                    if user_object_1.is_valid_date:
                        print('It is a valid date!')
                    else:
                        print('It is not a valid date')
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '5':
                try:
                    print(user_object_1.next_day)
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '0':
                exit()

