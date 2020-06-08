class IllegalCarError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

    def __str__(self):
        return "Wrong number entered! Remember car_mass must be <2000 and pax_count >= 1 and <=5"


class Car(object):
    def __init__(self, pax_count, car_mass, gear_count):
        if pax_count <1 or pax_count > 5:
            raise IllegalCarError()
        if car_mass > 2000:
            raise IllegalCarError()
        self._pax_count = pax_count
        self._car_mass = car_mass
        self._gear_count = gear_count
        self._total_mass = car_mass - 70

    @property
    def total_mass(self):
        return self._total_mass

    @property
    def car_mass(self):
        return self._car_mass - 70

    @property
    def pax_count(self):
        return self._pax_count

    @car_mass.setter
    def car_mass(self, value):
        if value > 2000:
            raise IllegalCarError()
        return self._car_mass

    @pax_count.setter
    def pax_count(self, value):
        if value <1 or value > 5:
            raise IllegalCarError()
        self._pax_count = value


c = Car(3, 1600, 5)
c.car_mass = 3030