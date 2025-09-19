class calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b

        elif self.operation == "sub":
            return self.a - self.b

        elif self.operation == "mul":
            return self.a * self.b

        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by Zero"
        else:
            return "Invalid operation!"

calc1 = calculator(45, 55, "add")
print("Result:", calc1.calculate())

calc1 = calculator(67, 32, "sub")
print("Result:", calc1.calculate())

calc1 = calculator(29, 5, "mul")
print("Result:", calc1.calculate())

calc2 = calculator(3.7, 5.5, "div")
print("Result:", calc2.calculate())

