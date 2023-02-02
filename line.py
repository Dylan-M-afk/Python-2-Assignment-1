from point import Point
import math


class Line(object):
    """A class representing a line, with two points on a cartesian plane

    Attributes:
        start_point: Point, starting point of the line in Point form
        end_point: Point, ending point of the line in Point form

    @Properties:
        start_point: getter
        end_point: getter and setter
        length: calculates the distance between start_point and end_point

    Methods:
        __lt__: allows checking if one lines' length is less than another lines' length
        __gt__: allows checking if one lines' length is greater than another lines' length
        __eq__: allows checking if one lines' length is equal to another lines length
        
    """
    def __init__(self, start_point: Point, end_point: Point) -> None:
        """constructs Line objects start and end point attributes

        Args:
            start_point (Point): starting point of a Line on a cartesian plane
            end_point (Point): ending point of a Line on a cartesian plane
        """
        assert isinstance(start_point, Point), 'start_point must of of type Point'
        assert isinstance(end_point, Point), 'end_point must be of type Point'
        self.__start_point = start_point
        self.__end_point = end_point

    @property
    def start_point(self):
        """getter property for start_point

        Returns:
            Point: the starting point of a Line
        """
        return self.__start_point

    @property
    def end_point(self):
        """getter property for end_point

        Returns:
            Point: the ending point of a Line
        """
        return self.__end_point

    @end_point.setter
    def end_point(self, new_end_point):
        """setter property for end_point

        Args:
            new_end_point (Point): _description_
        """
        self.__end_point = new_end_point

    @property
    def length(self):
        """calculates length of a Line using start_point and end_point

        Returns:
            float: calculated distance between start_point and end_point
        """
        distance = math.sqrt(
            ((self.start_point.x - self.end_point.x) ** 2) + (self.start_point.y - self.end_point.y) ** 2)
        return distance

    def __lt__(self, other):
        """allows use of < operator to compare to objects of the line class

        Args:
            other (Line): another object of type line to compare with

        Returns:
            bool: True if self.length < other.length, False otherwise
        """
        assert isinstance(other, Line), 'Can only compare with objects of the Line class'
        if self.length < other.length:
            return True
        return False

    def __gt__(self, other):
        """allows use of > operator to compare to objects of the line class

                Args:
                    other (Line): another object of type line to compare with

                Returns:
                    bool: True if self.length > other.length, False otherwise
        """
        assert isinstance(other, Line), 'Can only compare with objects of the Line class'
        if self.length > other.length:
            return True
        return False

    def __eq__(self, other):
        """allows use of == operator to compare to objects of the line class

            Args:
                    other (Line): another object of type line to compare with

            Returns:
                    bool: True if self.length == other.length, False otherwise
        """
        assert isinstance(other, Line), 'Can only compare with objects of the Line class'
        if self.length == other.length:
            return True
        return False


if __name__ == '__main__':
    while True:
        print()
        print('~~~Line Testing~~~')
        print('1: create a Line object')
        print('2: create a second Line object')
        print("3: print Line objects' length")
        print('4: compare both line objects to see if they are equal')
        print('5: compare both line objects to see if one is greater than')
        print('6: compare both line objects to see if one is less than')
        print('0: exit')
        print()
        user_choice = input('Enter your choice > ')
        match user_choice:
            case '1':
                while True:
                    try:
                        user_x_1 = float(input('Enter x coordinate for first point: '))
                        user_y_1 = float(input('Enter y coordinate for first point '))
                        user_x_2 = float(input('Enter x coordinate for second point: '))
                        user_y_2 = float(input('Enter y coordinate for second point '))
                        point1 = Point(user_x_1,user_y_1)
                        point2 = Point(user_x_2, user_y_2)
                        user_object_1 = Line(point1,point2)
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
                        user_x_1 = float(input('Enter x coordinate for first point: '))
                        user_y_1 = float(input('Enter y coordinate for first point '))
                        user_x_2 = float(input('Enter x coordinate for second point: '))
                        user_y_2 = float(input('Enter y coordinate for second point '))
                        point3 = Point(user_x_1, user_y_1)
                        point4 = Point(user_x_2, user_y_2)
                        user_object_2 = Line(point3, point4)
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
                            print(user_object_1.length)
                        case '2':
                            print(user_object_2.length)
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
            case '5':
                try:
                    compare = (user_object_1 > user_object_2)
                    match compare:
                        case True:
                            print('Object1 is greater than Object2')
                        case False:
                            print('Object1 is not greater than Object2')
                except NameError:
                    print('Please create both objects before comparison')
                except Exception as e:
                    print(e)
            case '6':
                try:
                    compare = (user_object_1 < user_object_2)
                    match compare:
                        case True:
                            print('Object1 is less than Object2')
                        case False:
                            print('Object1 is not less than Object2')
                except NameError:
                    print('Please create both objects before comparison')
                except Exception as e:
                    print(e)
            case '0':
                exit()