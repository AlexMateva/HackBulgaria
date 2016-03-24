from random import randint


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "{} {} with max speed of: {}".format(self.car, self.model, self.max_speed)

    def __int__(self):
        return(self.max_speed)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return "{} drives {} {} ".format(self.name, self.car.car, self.car.model)

    def __repr__(self):
        return self.__str__()


class Race():
    def __init__(self, drivers, crash_chance):
        self.drivers = [driver.name for driver in drivers]
        self.crash_chance = crash_chance
        self.crashed = False

    def __getitem__(self, index):
        return self._drivers[index]

    def crash(self):
        num = randint(1, 10)
        if self.crash_chance * num > 5:
            self.crashed = True
            print("Unfortunately, {} has crashed.".format(self.drivers.name))

    # def result(self):
    #     result = []
    #     a, b, c, d = self.drivers[0], self.drivers[1], self.drivers[2], self.drivers[3]
    #     a1 = a.car.max_speed * randint(1, 10)
    #     b1 = b.car.max_speed * randint(1, 10)
    #     c1 = c.car.max_speed * randint(1, 10)
    #     d1 = d.car.max_speed * randint(1, 10)


class Championship:
    def __init__(self, name, races_count, races):
        self.name = name
        self.races_count = races_count
        self.races = [race.name for driver in drivers]

    def __str__(self):
        return "{} has {} races".format(self.name, self.races_count)

    def top3(self, )


