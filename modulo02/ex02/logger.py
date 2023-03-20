import time
from random import randint
import os

def log(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        run = function(*args, **kwargs)
        total = time.perf_counter() - start
        if (total < 1.0):
            total = f"[exec-time {(total * 1000):.3f} ms ]"
        else:
            total = f"[ exec-time {(total):.3f} s ]"
        user = os.environ["USER"]
        task = function.__name__.replace("_", " ").title()
        log = (f"({user})Running: {task: <19}{total}\n")
        file = open("machine.log", "a")
        file.write(log)
        file.close
        return run
    return wrapper

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
if __name__ == "__main__":
        machine = CoffeeMachine()
        for i in range(0, 5):
            machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)