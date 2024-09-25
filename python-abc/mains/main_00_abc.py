from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self) -> str:
        """Return the sound the animal makes.

        This method should be overridden by subclasses to provide
        the specific sound the animal makes.
        """
        pass

class Dog(Animal):
    """Concrete class for a dog."""

    def sound(self) -> str:
        """Return the sound a dog makes.

        Returns:
            str: The sound "Woof!"
        """
        return "Woof!"

class Cat(Animal):
    """Concrete class for a cat."""

    def sound(self) -> str:
        """Return the sound a cat makes.

        Returns:
            str: The sound "Meow!"
        """
        return "Meow!"

