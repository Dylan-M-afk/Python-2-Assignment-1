class Point(object):
    """a class represents a point using two coordinates, x and y 

    Attributes:
            x : float
                x coordinate of the point
            y : float
                y coordinate of the point

    @Properties:
        x:getter
        y:getter
    """

    def __init__(self, x: float, y: float) -> None:
        """constructs the x and y attributes for point object 

        Args:
            x (float): _description_
            y (float): _description_
        """
        assert isinstance(x, float), 'x must be a float'
        assert isinstance(y, float), 'y must be a float'
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        """returns x,y coordinates in string form

        Returns:
            str: (x, y)
        """
        return f'({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        """evaluates if one point is the same as another

        Args:
            other (Point): object to compare to, must be of type Point

        Returns:
            bool: True if both points are the same, False if not
        """
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False

    @property
    def x(self):
        """getter property for coordinate x

        Returns:
            float: private value x
        """
        return self.__x

    @property
    def y(self):
        """getter property for coordinate y

        Returns:
            float: private value y
        """
        return self.__y


if __name__ == '__main__':
    while True:
        print()
        print('~~~Point Testing~~~')
        print('1: create a Point object')
        print('2: create a second Point object')
        print('3: print Point object')
        print('4: compare both point objects to see if they are equal')
        print('0: exit')
        print()
        user_choice = input('Enter your choice > ')
        match user_choice:
            case '1':
                while True:
                    try:
                        user_x = float(input('Enter x coordinate: '))
                        user_y = float(input('Enter y coordinate: '))
                        user_object_1 = Point(user_x, user_y)
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
                while True:
                    try:
                        user_x = float(input('Enter x coordinate: '))
                        user_y = float(input('Enter y coordinate: '))
                        user_object_2 = Point(user_x, user_y)
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
            case '3':
                try:
                    object_to_print = input('Enter the object number to print (1 or 2): ')
                    match object_to_print:
                        case '1':
                            # Will cause NameError if not created yet
                            print(user_object_1)
                        case '2':
                            print(user_object_2)
                        case _:
                            print('Not a valid object number')
                except NameError:
                    print('You must create that object first!')
                except Exception as e:
                    print(e)
            case '4':
                try:
                    compare = (user_object_1 == user_object_2)
                    match compare:
                        case True:
                            print('Both objects are the same!')
                        case False:
                            print('Both objects are not the same')
                except NameError:
                    print('Please create both objects before comparison')
                except Exception as e:
                    print(e)
            case '0':
                exit()
