from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass
class Engine(GearBox):


    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def set_gear(self):
        print("Gearbox is ready")


    def drive(self):
        self.start()
        self.set_gear()
        self.stop()


car_obj = Car()
car_obj.drive()