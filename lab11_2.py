from tkinter import *


class Car:
    make = "Honda"
    type = ""

    def __init__(self, type):
        self.type = type

    def show(self):
        return 'is a car!'


class Van(Car):
        def show(self):
            return 'is a mini Van!'


class SUV(Car):
        def show(self):
            return 'is a SUV!'


class Sedan(Car):
        def show(self):
            return 'is a Sedan!'

car1 = Van('Odyssey')
car2 = SUV('Pilot')
car3 = Sedan('Civic')
car4 = Sedan('Avalon')
car4.make = "Toyota"

s = ""
for myCar in [car1, car2, car3, car4]:
    s += myCar.make + " " + myCar.type + " " + myCar.show() + "\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
