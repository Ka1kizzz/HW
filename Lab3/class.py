#ex1
class mystring:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())
ruru = mystring()
ruru.getString()
ruru.printString()

#ex2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print(shape.area())
square = Square(5)
print(square.area())

#ex3
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
rectangle = Rectangle(10, 15)
print(rectangle.area())

#ex4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point ({}, {})".format(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

p = Point(3, 4)
p.show()
p.move(1, 2)
p.show()
q = Point(5, 6)
print(p.dist(q))
#ex5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of {} successful. New balance is {}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal of {} successful. New balance is {}".format(amount, self.balance))



account = Account("Nurbergen Turagal", 100)

account.deposit(200000)

account.withdraw(45300)

account.withdraw(0)
#ex6
PrimeN = lambda n:n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

primes = list(filter(PrimeN, numbers))

print("List of prime numbers:", primes)


