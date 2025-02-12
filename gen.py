#1
def squ(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input("Enter a number n: "))
for i in squ(n):
    print(i, end=' ')
#2
def ev(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number n: "))
en = ev(n)
print(", ".join(map(str, en)))

#3
def di(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number n: "))
for num in di(n):
    print(num, end=' ')

#4
def sq(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
for s in sq(a, b):
    print(s, end=' ')

#5
def cnt(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter a number n: "))
for n in cnt(n):
    print(n, end=' ')

