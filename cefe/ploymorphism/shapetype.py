from shape import shape

class Square(shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Square'

class Cricle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Circle'

class Triangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Triamgle'

