import time
from math import sqrt, pi
from math import pi
class CalculatorOrigin:
    pass
class Calculator(CalculatorOrigin):
    def run(self):
        while True:

            print("Calculator Loading")
            time.sleep(1) #Loading   Sim
            print("...")  #Print Loading
            time.sleep(1) # Loading Sim
            print("...")  #"..."


            time.sleep(1)
            print("Welcome to Calculator")
            inp = input("Number->")
            otherinp = input("Number->")

            op = input("Operation: A = +, B = -, C = *, D = / ->")
            if op == "A":
                print((int(inp) + int(otherinp)))
            if op == "B":
                print(float(inp) - int(otherinp))
            if op == "C":

                print("Result:", int(inp) * int(otherinp))
            if op == "D": # D for division
                print("answer:", str(int(inp) / (int(otherinp))))

            else:
                print("incorrect")
                break

Calculator().run()

