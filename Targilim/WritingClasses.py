class Car:
    def __init__(self, model, number, color, year):
        self._model = model
        self._number = number
        self._color = color
        self._year = year

    def details(self):
        print(self._model, self._number, self._color, self._year)


class Jeep(Car):
    def __init__(self, model, number, color, year, times_four, height):
        Car.__init__(self, model, number, color, year)
        self._times_four = times_four
        self._height = height

    def details(self):
        print(self._model, self._number, self._color, self._year, self._times_four, self._height)


j1 = Jeep("wrangler", 123456789, "black", 2019, True, 170)
c1 = Car("wrangler", 123456789, "black", 2019)
j1.details()
c1.details()






