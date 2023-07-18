# Basic Calculator, 18/07/23 
# Done by Florencia Zoffi

class Calculator: 
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def add(self):
        return self.n + self.m

    def sub(self):
        return self.n + self.m

    def divide(self):
        if self.m != 0:
            return self.n / self.m
        else:
            message = 'It is not possible to divide by 0'
            return message

    def mult(self):
        return self.n * self.m


def main():
    print("""
    Select an operation to be done:
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
    5. Exit
    """)

    choice = float(input('Enter a number between 1 to 5: '))

    while choice < 1 or choice > 5:
        print('The number chosen is not valid')
        print("""
    Select an operation to be done:
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
    5. Exit
        """)
        choice = float(input('Please enter a number between 1 to 5: '))

    if choice == 5: 
        print('See you later!')
        exit()

    n = float(input('Provide the first number: '))
    m = float(input('Provide the second number: '))
    calculator = Calculator(n, m)

    if choice == 1:
        print(f'The result of the addition of {n} and {m} is: {calculator.add()}')
    elif choice == 2:
        print(f'The result of the subtraction of {n} and {m} is: {calculator.sub()}')
    elif choice == 3:
        print(f'The result of the division of {n} and {m} is: {calculator.divide()}')
    elif choice == 4:
        print(f'The result of the multiplication of {n} and {m} is: {calculator.mult()}')

if __name__ == "__main__":
    main()