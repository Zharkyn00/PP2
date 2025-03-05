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

text = "Hello World!"
upper, lower = count_letters(text)

print("Upper case letters:", upper)
print("Lower case letters:", lower)

# 3
def task3(s):
    return s == s[::-1]

print(task3("radar"))  # True
print(task3("hello"))  # False

# 4
def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == "".join(reversed(s)) 

word1 = "madam"
word2 = "hello"

print(f'Is "{word1}" a palindrome?', is_palindrome(word1))
print(f'Is "{word2}" a palindrome?', is_palindrome(word2))


# 5
def all_true(t):
    r = True
    for v in t:
        r = r and v  
    return r

t1 = (True, True, True)
t2 = (True, False, True)

print(all_true(t1))  # True
print(all_true(t2))  # False

