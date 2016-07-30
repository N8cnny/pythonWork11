from tkinter import *

global s
s = "result:\n"


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        return self.data

x = FirstClass()
y = FirstClass()

x.setdata("CIS247")
y.setdata(3.14159)

s += x.__class__.__name__ + ": " + x.display() + "\n"
s += y.__class__.__name__ + ": " + str(y.display()) + "\n"


class SecondClass(FirstClass):
    def display(self):
        return self.data

z = SecondClass()
z.setdata(42)
s += z.__class__.__name__ + ": " + str(z.display()) + "\n"
s += x.__class__.__name__ + ": " + x.display() + "\n"


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __mul__(self, other):
        self.data = self.data * other

a = ThirdClass("cis")
s += a.__class__.__name__ + ": " + a.display() + "\n"

b = a + '247'
s += b.__class__.__name__ + ": " + b.display() + "\n"

a * 3
s += a.__class__.__name__ + ": " + a.display() + "\n"


root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
