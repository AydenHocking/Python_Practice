# Calculator class evaluates input into add, subtract, multiply, or divide(with /0 error check)
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b


def main():
    while True:
        try:
            # Input values and operator
            numberA = float(input("Enter a number: "))
            operator = input("Enter operator: (+,-,/,*) ")
            numberB = float(input("Enter another number: "))
            # Machine instance
            calculator = Calculator(numberA, numberB)
            # Operator checks
            if operator == "+":
                solution = calculator.add()
            elif operator == "-":
                solution = calculator.subtract()
            elif operator == "*":
                solution = calculator.multiply()
            elif operator == "/":
                solution = calculator.divide()
            else:
                print("Error: Invalid operator")
                continue
            # Print solution
            print(str(solution))
        except ValueError:
            print("Error: Invalid number")
            continue

if __name__ == "__main__":
    main()


