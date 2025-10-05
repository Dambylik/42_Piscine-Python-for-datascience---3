from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Hail King Joffrey"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for King, inherits from
        Baratheon and Lannister."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Return the eye color"""
        return self.eyes

    def set_eyes(self, color: str):
        """Set the eye color"""
        self.eyes = color

    def get_hairs(self):
        """Return the hair color"""
        return self.hairs

    def set_hairs(self, color: str):
        """Set the hair color"""
        self.hairs = color
