import math


class Circle(object):
    """a class to represent a Circle object with radius and color

    Attributes:
        radius : float, radius size of the Circle
        color : string, color of the Circle

    @Properties:
        radius: setter and getter
        color: setter and getter

    Methods:
        get_area():  
            Returns (float): area of circle
            
        get_circumference():
            returns (float): circumference of circle
        
    """

    def __init__(self, radius=1.0, color='Red') -> None:
        """constructs all attributes for Circle object

        Args:
            radius (float): radius of the circle. Defaults to 1.0.
            color (str): color of the circle. Defaults to 'Red'.
        """

        assert isinstance(radius, float), 'radius must be a float'
        assert radius > 0
        assert isinstance(color, str), 'color must be a str'
        self.__radius = radius
        self.__color = color

    def __str__(self) -> str:
        """returns string form of the radius

        Returns:
            str: radius as a string using getter
        """

        return f'{self.radius}'

    @property
    def radius(self):
        """getter property for radius of a Circle object

        Returns:
            float: Circle object's radius value
        """

        return self.__radius

    @radius.setter
    def radius(self, new_radius: float):
        """setter property for radius of Circle object

        Args:
            new_radius (float): Value to set radius value to

        Raises:
            TypeError: new_radius must be float
            ValueError: new_radius value must be > 0
        """

        if type(new_radius) != float:
            raise TypeError('new_radius must be a float')
        if new_radius <= 0:
            raise ValueError('new_radius value must be greater than 0')
        self.__radius = new_radius

    @property
    def color(self):
        """getter property for color of Circle object

        Returns:
            str: Circle object's color value
        """

        return self.__color

    @color.setter
    def color(self, new_color: str):
        """setter property for color of Circle object

        Args:
            new_color (str): value to set objects color value

        Raises:
            TypeError: new_color must be a string
        """

        if type(new_color) != str:
            raise TypeError('new_color must be a string')
        self.__color = new_color

    def get_area(self):
        """gets the area of a circle object

        Returns:
            float: area of Circle object using (pi * (r * r)
        """

        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        """gets the circumference of a Circle object

        Returns:
            float: circumference of Circle object using (2 * pi * R)
        """

        return (2 * math.pi) * self.radius


if __name__ == '__main__':
    while True:
        print()
        print('~~~Circle Testing~~~')
        print('1: Create a circle object')
        print('2: Change circle radius')
        print('3: Change circle color')
        print('4: Get circle area')
        print('5: Get circle circumference')
        print('6: Print radius')
        print('7: Print color')
        print()
        user_choice = input('Enter your choice > ')
        match user_choice:
            case '1':
                # Get correct input from user
                while True:
                    try:
                        user_radius = float(input('Enter Radius (float): '))
                        user_color = input('Enter color: ')
                    except TypeError as te:
                        print(te)
                    except ValueError as ve:
                        print('Please enter a number!')
                    else:
                        break
                # Create the Circle object, with hopefully no incorrect data
                try:
                    user_circle = Circle(radius=user_radius, color=user_color)
                except TypeError as te:
                    print(te)
                except ValueError as ve:
                    print(ve)
                except AssertionError as ae:
                    print(ae)
            case '2':
                # Get a new radius from user to assign to circle
                while True:
                    try:
                        user_new_radius = float(input('Enter new radius: '))
                    except ValueError as ve:
                        print('Please enter a number')
                    except Exception as e:
                        print(e)
                    else:
                        break
                # use setter to assign new radius
                try:
                    user_circle.radius = user_new_radius
                except NameError as ne:
                    print('You must create a circle first')
                except TypeError as te:
                    print(te)
                except ValueError as ve:
                    print(ve)
                except AssertionError as ae:
                    print(ae)
                except Exception as e:
                    print(e)
                else:
                    print(f'radius updated to {user_new_radius}')
            case '3':
                # Get a color from user to assign radius to
                while True:
                    try:
                        user_new_color = input('Enter new radius: ')
                    except Exception as e:
                        print(e)
                    else:
                        break
                # use setter to assign new color
                try:
                    user_circle.color = user_new_color
                except TypeError as te:
                    print(te)
                except ValueError as ve:
                    print(ve)
                except AssertionError as ae:
                    print(ae)
                except NameError as ne:
                    print('You must create a circle first')
                except Exception as e:
                    print(e)
                else:
                    print(f'color updated to {user_new_color}')
            case '4':
                try:
                    print(f"Your circle's area is: {user_circle.get_area()}")
                except NameError as ne:
                    print('You must create a circle first')
                except Exception as e:
                    print(e)
            case '5':
                try:
                    print(f"Your circle's circumference is: {user_circle.get_circumference()}")
                except NameError as ne:
                    print('You must create a circle first')
                except Exception as e:
                    print(e)
            case '6':
                # Uses __str__
                try:
                    print(user_circle)
                except NameError as ne:
                    print('You must create a circle first')
                except Exception as e:
                    print(e)
            case '7':
                try:
                    print(user_circle.color)
                except NameError as ne:
                    print('You must create a circle first')
                except Exception as e:
                    print(e)
            case '0':
                break
