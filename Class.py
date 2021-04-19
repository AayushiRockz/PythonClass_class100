class Car(object):
    def __init__(self,colour, model, speed, company):
        self.colour = colour
        self.model = model 
        self.speed = speed
        self.company = company

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("accelerating")

    def changeGear(self, gearType):
        print("gear changed", gearType)


audi = Car("red","3","50","audi")
print(audi.colour)
audi.start()
audi.changeGear(2)