class Car:
    sterringWheel = 1; #class level attribute
    def __init__(self, name, wheels): #instence level
        self.name = name;
        self.wheels = wheels;
    
    def startEngine(self):
        print(f'{self.name} started enginge');

    def drive(self):
        print(f'{ self.name } is driving');

    @classmethod #class level method
    def common(cls):
        print(f'All cars have only {cls.sterringWheel} sterring wheel.');

# car = Car('Marcedies', 4);
# car.startEngine();
# car.drive();

# Car.common();