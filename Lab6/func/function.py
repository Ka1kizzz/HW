#ex1
from functools import reduce
def multiply(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result


numbers = [2, 3, 4, 5]

result = multiply(numbers)

print(result)

#ex2
def counter(input_string):
    up = sum(1 for char in input_string if char.isupper())
    low = sum(1 for char in input_string if char.islower())

    return up, low



input_string = input("Enter a string: ")

up, low = count_upper_lower_letters(input_string)

print(up)
print(low)

#ex3
def pali(string):

    string = string.replace(" ", "").lower()


    return string == string[::-1]



string = input("Enter a string: ")


if pali(string):
    print("palindrome.")
else:
    print("not a palindrome.")

#ex4
import time
import math

def calculator(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

chislo = 25100
millisec = 2123

result = calculator(chislo, millisec)

print(f"Square root of {chislo} after {millisec} milliseconds is {result}")


#ex5
def trueE(tuple_data):
    return all(tuple_data)

tuple_data = (True, True, False, True)

result = trueE(tuple_data)

if result:
    print("All TRUE")
else:
    print("Not all TRUE")
