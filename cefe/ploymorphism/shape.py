from turtle import shape


class Shape:
    def __init__(self) -> None:
        self.__shape = shape
        self.__area = 0
        @popperty
        def shape(self):
            return self.__shape

        @shape.settre
        def shape(self,shape):
            self.shape = shape

        @property
        def area(self):
            return self.___area

        @area.setter
        def area(self,value):

        def compute_area(self):
            pass
        