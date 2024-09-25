#!/usr/bin/env python3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        from task_04_flyingfish import Fish, FlyingFish
    except ImportError as e:
        logging.error(f"Error importing module: {e}")
        return

    try:
        flying_fish = FlyingFish()
        flying_fish.swim()
        logging.info("Flying fish is swimming.")
        flying_fish.fly()
        logging.info("Flying fish is flying.")
        flying_fish.habitat()
        logging.info("Flying fish habitat information displayed.")
    except Exception as e:
        logging.error(f"Error executing methods: {e}")

if __name__ == "__main__":
    main()

