#!/usr/bin/env python3

from task_05_dragon import Dragon

def main() -> None:
    """
    Main function to demonstrate the Dragon class methods.
    """
    dragon = Dragon()

    try:
        dragon.swim()  # Outputs: The creature swims!
        dragon.fly()   # Outputs: The creature flies!
        dragon.roar()  # Outputs: The dragon roars!
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

