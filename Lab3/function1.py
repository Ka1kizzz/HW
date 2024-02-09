#ex1
def myfunction(grams):
    ounces = 28.3495231 * grams
    print(ounces)
myfunction(45)

#ex2
def myfunct():
    F = float(input())
    C = (5 / 9) * (F - 32)
    print(C)
myfunct()

#ex3
def solve(numheads, numlegs):
    num_chickens = 0
    num_rabbits = 0

    for chickens in range(numheads + 1):

        chickenlegs = chickens * 2

        rabbitlegs = (numheads - chickens) * 4

        if chickenlegs + rabbitlegs == numlegs:
            num_chickens = chickens
            num_rabbits = numheads - chickens
            break


    return num_chickens, num_rabbits

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print("chickens:", result[0])
print("rabbits:", result[1])

#ex4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):

    return [num for num in numbers if is_prime(num)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("PrimeN:", filter_prime(numbers))

#ex5
from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)
    for perm in perms:
        print(''.join(perm))

input_string = input()
print()
print_permutations(input_string)

#ex6
def reversedwords(input_string):
    words = input_string.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
input_sentence = input()
print(reversedwords(input_sentence))

#ex7
def has_adjacent_three(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

numbers = [int(x) for x in input().split()]
print(has_adjacent_three(numbers))

#ex8
def contains_007(nums):
    zeros = [i for i, x in enumerate(nums) if x == 0]
    sevens = [i for i, x in enumerate(nums) if x == 7]
    return len(zeros) >= 2 and len(sevens) >= 1 and zeros[0] < zeros[-1] < sevens[-1]

numbers = [1, 2, 0, 0, 7, 8]
print(contains_007(numbers))

#ex9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input())
print(sphere_volume(radius))

#ex10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(input_list)
print(unique_elements(input_list))
#ex11
def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()

    return cleaned_word == cleaned_word[::-1]

input_word = input()
if is_palindrome(input_word):
    print("Palindrome.")
else:
    print("Not palindrome.")

#ex12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])

#ex13

