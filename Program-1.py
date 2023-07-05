class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'addition':
            result = self.a + self.b
        elif self.operation == 'subtraction':
            result = self.a - self.b
        elif self.operation == 'multiplication':
            result = self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                result = self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation. Please choose from 'addition', 'subtraction', 'multiplication', or 'division'."

        return result
#Example 
a = 8.9
b = 5.7
operation = 'subtraction'

calc = Calculator(a, b, operation)
result = calc.calculate()
print(f"The result of {operation} is: {result}")
