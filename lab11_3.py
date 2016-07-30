from tkinter import *


class ParentA:
    msg = ""

    def __init__(self):
        self.msg = "I am the parent A."

    def __del__(self):
        print("Clear the parent A.")


class ParentB:
    msg = ""

    def __init__(self):
        self.msg = "I am the parent B."


class ChildA(ParentA):
    msg = ""

    def __init__(self):
        self.msg = "I am the child of A. I inherit Parent A. Child A rules."

    def __del__(self):
        print("clear the child A.")


class ChildB(ParentA):
    msg = ""

    def __init__(self):
        self.msg = "I am the child of B. I inherit Parent A. Child B rules."


class ChildC(ParentA):
    pass


class ChildD(ParentB):
    msg = ""

    def __init__(self):
        self.msg = "I am the child of D. I inherit Parent B. Child D rules."

    def __del__(self):
        print("clear the child D.")


class ChildE(ParentB):
    msg = ""

    def __init__(self):
        self.msg = "I am the child of E. I inherit Parent B. Child E rules."


class ChildF(ParentB):
    pass

Mother = ParentA()
Father = ParentB()
John = ChildA()
Jane = ChildB()
Jack = ChildC()
Judy = ChildD()
James = ChildE()
Jenny = ChildF()

s = "ObjectID\tClass Type\tMessage\n"
s += "Mother\t" + str(type(Mother)) + "\t" + Mother.msg + "\n"
s += "Father\t" + str(type(Father)) + "\t" + Father.msg + "\n"
s += "John\t" + str(type(John)) + "\t" + John.msg + "\n"
s += "Jane\t" + str(type(Jane)) + "\t" + Jane.msg + "\n"
s += "Jack\t" + str(type(Jack)) + "\t" + Jack.msg + "\n"
s += "Judy\t" + str(type(Judy)) + "\t" + Judy.msg + "\n"
s += "James\t" + str(type(James)) + "\t" + James.msg + "\n"
s += "Jenny\t" + str(type(Jenny)) + "\t" + Jenny.msg + "\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
