class calculator:
    """Calculator class for vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        result = sum(V1[i] * V2[i] for i in range(len(V1)))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the addition of two vectors."""
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the subtraction of two vectors."""
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {result}")
