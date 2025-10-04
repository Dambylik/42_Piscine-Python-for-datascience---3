from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class of a generic character"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Change the character's state to dead."""
        self.is_alive = False


class Stark(Character):
    """A member of the Stark family"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark, inherits Character."""
        super().__init__(first_name, is_alive)
