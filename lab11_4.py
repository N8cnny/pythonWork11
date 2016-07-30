import InputBox
from tkinter import *


class Lexus:
    make = "Lexus"
    length = "191.1 in"
    weight = "3,472 lb"
    cylinder = "3.3-liter V6"
    model = ""
    color = ""

    def enginestart(self):
        return "Engine started...\n"

    def run(self):
        return "Running...\n"

    def enginestop(self):
        return "Stopped...\n"

    def __init__(self, model, color):
        self.color = color
        self.model = model

    def showspec(self):
        result = self.make + "\n" + self.length + "\n" + self.weight + "\n"
        result += self.cylinder + "\n" + self.model + "\n" + self.color + "\n"
        return result

    def testdrive(self):
        InputBox.ShowDialog("Do you want a test drive ['y/n']: ")
        tryit = InputBox.GetInput()
        if tryit.lower() == 'y':
            result = self.enginestart() + self.run() + self.enginestop()
            return result
        else:
            return "Good bye!\n"

InputBox.ShowDialog("Enter the model ['GX', 'TX', or 'MX']: ")
model = InputBox.GetInput()

s = ""
if model.lower() == "gx":
    gx = Lexus("GX", "Silver")
    s += gx.showspec() + "\n"
    s += gx.testdrive() + "\n"
elif model.lower() == "tx":
    tx = Lexus("TX", "Grey")
    s += tx.showspec() + "\n"
    s += tx.testdrive() + "\n"
elif model.lower() == "mx":
    mx = Lexus("MX", "White")
    s += mx.showspec() + "\n"
    s += mx.testdrive() + "\n"
else:
    s += "Invalid entry.\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
