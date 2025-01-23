from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class LandAnimal(Animal):
    def make_sound(self):
        return "LandAnimal sound"


class WaterAnimal(Animal):
    def make_sound(self):
        return "WaterAnimal sound"


class Amphibian(LandAnimal, WaterAnimal):
    def make_sound(self):
        land_sound = LandAnimal.make_sound(self)
        water_sound = WaterAnimal.make_sound(self)
        return f"{land_sound} & {water_sound}"


if __name__ == '__main__':
    land = LandAnimal()
    water = WaterAnimal()
    frog = Amphibian()

    print("LandAnimal:", land.make_sound())
    print("WaterAnimal:", water.make_sound())
    print("Amphibian:", frog.make_sound())