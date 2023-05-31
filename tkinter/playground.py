def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate(n, **kwargs):
    # print(kwargs)
    # for (key, value) in kwargs.items():
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(n=2, add=3, multiply=5)
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
