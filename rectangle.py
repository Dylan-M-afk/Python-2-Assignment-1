from point import Point
from line import Line


class Rectangle(object):
    """A class to represent a rectangle object using two points on a cartesian plane

    Attributes:
            bottom_left_corner : Point
            top_right_corner : Point
    
    @Properties:
            bottom_left_corner 
                returns bottom_left_corner of the rectangle
            bottom_right_corner 
                returns bottom_right_corner of the rectangle
            top_right_corner 
                returns top_right_corner of the rectangle
            top_left_corner 
                returns top_left_corner of the rectangle
            area
                returns the area of the rectangle
            perimeter
                returns the perimeter of the rectangle
        
    """
    def __init__(self, bottom_left_corner: Point, top_right_corner: Point) -> None:
        """constructs the bottom_left and bottom_right attributes for point object 

        Args:
            bottom_left_corner (Point): _description_
            top_right_corner (Point): _description_
        """
        assert type(bottom_left_corner) == Point
        assert type(top_right_corner) == Point
        self.__bottom_left_corner = bottom_left_corner
        self.__top_right_corner = top_right_corner

    @property
    def bottom_left_corner(self):
        """getter property for bottom left corner Point of rectangle object

        Returns:
            Point: Private Point object
        """
        return self.__bottom_left_corner

    @property
    def top_right_corner(self):
        """getter property for top right corner Point of rectangle object

        Returns:
            Point: Private Point object
        """
        return self.__top_right_corner

    @property
    def bottom_right_corner(self):
        """getter property for bottom right corner Point of rectangle object

        Returns:
            Point: Point object that is calculated with top right x, and bottom left y
        """
        bottom_right_corner = Point(self.top_right_corner.x, self.bottom_left_corner.y)
        return bottom_right_corner

    @property
    def top_left_corner(self):
        """getter property for top left corner Point of rectangle object

        Returns:
            Point: Point object that is calculated with bottom left x, and top right y
        """
        top_left_corner = Point(self.bottom_left_corner.x, self.top_right_corner.y)
        return top_left_corner

    @property
    def area(self):
        """Calculates and returns the area of the Rectangle object

        Returns:
            Float: calculated by creating a width and height line and multiplying them
        """
        w = Line(self.bottom_left_corner, self.top_left_corner)
        l = Line(self.bottom_left_corner, self.bottom_right_corner)
        return w.length * l.length

    @property
    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle object

        Returns:
            Float: calculated by multiplying a width and height line then multiplying them by 2,
        """
        w = Line(self.bottom_left_corner, self.top_left_corner)
        l = Line(self.bottom_left_corner, self.bottom_right_corner)
        return 2 * (w.length + l.length)


if __name__ == '__main__':
    while True:
        print()
        print('~~~Rectangle Testing~~~')
        print('1: create a Rectangle object')
        print('2: print each corner')
        print('3: print rectangle area')
        print('4: print rectangle perimeter')
        print('0: exit')
        print()
        user_choice = input('Enter your choice > ')
        match user_choice:
            case '1':
                while True:
                    try:
                        user_x_1 = float(input('Enter x coordinate for bottom left corner: '))
                        user_y_1 = float(input('Enter y coordinate for bottom left corner: '))
                        user_x_2 = float(input('Enter x coordinate for top right corner: '))
                        user_y_2 = float(input('Enter y coordinate for top right corner: '))
                        point1 = Point(user_x_1, user_y_1)
                        point2 = Point(user_x_2, user_y_2)
                        user_object = Rectangle(point1, point2)
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
                    print("(X, Y)")
                    print(f"Top Left:{user_object.top_left_corner}")
                    print(f"Top Right:{user_object.top_right_corner}")
                    print(f"Bottom Left:{user_object.bottom_left_corner}")
                    print(f"Bottom Right:{user_object.bottom_right_corner}")
                except NameError:
                    print("Please create an object first!")
                except Exception as e:
                    print(e)
            case '3':
                try:
                    print(f'The area of your created Rectangle object is: {user_object.area}')
                except NameError:
                    print('Please create the Rectangle object first!')
                except Exception as e:
                    print(e)
            case '4':
                try:
                    print(f'The perimeter of your created Rectangle object is: {user_object.perimeter}')
                except NameError:
                    print('Please create the Rectangle object first!')
                except Exception as e:
                    print(e)
            case '0':
                exit()
