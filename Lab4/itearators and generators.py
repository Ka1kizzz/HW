#ex1
def square_generator(N):
    for i in range(1, N+1):
        yield i**2

N = int(input())
for square in square_generator(N):
    print(square)

#ex2
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())

for num in even_numbers(n):
    print(num, end=', ')

#ex3
def gen34(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())

for num in gen34(n):
    print(num,end=', ')

#ex4
def square_generator2(a,b):
    for i in range(a,b):
        if i >= a and b:
            yield i**2
a = int(input())
b = int(input())
for num in square_generator2(a,b):
    print(num, end=', ')

#ex5
def MrReturn(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for num in MrReturn(n):
    print(num, end=' ')
