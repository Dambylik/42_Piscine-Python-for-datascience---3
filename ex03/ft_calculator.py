class calculator:
    """Calculator class for vector-scalar operations."""

    def __init__(self, vector: list[float]):
        """Initialize with a list of floats."""
        self.vector = vector

    def __add__(self, object: int | float) -> None:
        """Add a scalar to each element of the vector."""
        if isinstance(object, (int, float)):
            new_list = []
            for value in self.vector:
                new_list.append(value + object)
            self.vector = new_list
            print(self.vector)
        else:
            print("Error: object must be an int or float")

    def __mul__(self, object: int | float) -> None:
        """Multiply each element of the vector by a scalar."""
        if isinstance(object, (int, float)):
            new_list = []
            for value in self.vector:
                new_list.append(value * object)
            self.vector = new_list
            print(self.vector)
        else:
            print("Error: object must be an int or float")

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector."""
        if isinstance(object, (int, float)):
            new_list = []
            for value in self.vector:
                new_list.append(value - object)
            self.vector = new_list
            print(self.vector)
        else:
            print("Error: object must be an int or float")

    def __truediv__(self, scalar: int | float) -> None:
        """Divide each element of the vector by a scalar."""
        if isinstance(scalar, (int, float)) and scalar != 0:
            new_list = []
            for value in self.vector:
                result = value / scalar
                new_list.append(result)
            self.vector = new_list
            print(self.vector)
        else:
            print("Error: operand must be a non-zero int or float")
