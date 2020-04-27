import time
from random import randint
import os


class CoffeeMachine():
    water_level = 100

    def log(func):
        def inner(self, *args):
            begin = time.time()
            ret = func(self, *args)
            end = time.time()
            login = os.getlogin()
            with open("machine.log", "a") as f:
                if end - begin < 1:
                    f.write("({:s})Running : {:20s} [exec-time : {:.3f}\
 {:3s}]\n".format(login, func.__name__, 1000 * (end - begin), "ms"))
                else:
                    f.write("({:s})Running : {:20s} [exec-time : {:.3f}\
 {:3s}]\n".format(login, func.__name__, end - begin, "s"))
            f.close()
            return ret
        return inner

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
            for i in range(20):
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
