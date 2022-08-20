#*args: Positional Variable-Length Arguments
def add(*args):
    print(args) # (3, 5, 6, 2, 1, 7, 4, 3)
    print(type(args))

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 2, 1, 7, 4, 3))

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs) # {'add': 3, 'multiply': 5}
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs.keys()) # dict_keys(['add', 'multiply'])
    print(kwargs.values()) # dict_values([3, 5])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make='Hyndai', model='i10') # here i can create a car using any no of keyword argument
print(my_car.model)  # no need to pass all attributes- make, model, color,.. since Function definition **kw is mentioned
