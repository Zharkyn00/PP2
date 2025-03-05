import math
import time
import functools

# 1
def task1(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

print(task1([1, 2, 3, 4]))  # 24

# 2
def task2(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

print(task2("HelloWorld"))  # (2, 8)

# 3
def task3(s):
    return s == s[::-1]

print(task3("radar"))  # True
print(task3("hello"))  # False

# 4
def task4(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

print(task4(25100, 2123))  # 158.42979517754858 (және кідіріс 2.123 секунд)

# 5
def task5(tpl):
    return all(tpl)

print(task5((True, True, False)))  # False
print(task5((1, "hello", 3.5)))  # True
