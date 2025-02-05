#1
def grams_to_ounces(grams):
	return 28.3495231 * grams
grams = float(input("Enter weight in grams: "))
print(f"{grams} grams is equal to {grams_to_ounces(grams)} ounces.")

#2
import math
def centigrade(fahrenheit):
	return (5/9)*(fahrenheit-32)
fahrenheit = float(input())
print(f"Fahrenheit in centigrade is: {centigrade(fahrenheit)}")

#3
def solve(numheads, numlegs):
	x = (4 * numheads - numlegs) // 2
	y = numheads - x
	if x < 0 or y < 0 or 2 * x + 4 * y != numlegs:
		return "No valid solution"
	return f"Chickens: {x}, Rabbits: {y}"
numheads = 35
numlegs = 94
print(solve(numheads, numlegs))

#4
def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True
def filter_prime(numbers):
	prime_numbers = []
	for num in numbers:
		if is_prime(num):
			prime_numbers.append(num)
	return prime_numbers
numbers = list(map(int, input().split()))
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

#5
from itertools import permutations
def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print("".join(perm))
user_input = input("Enter a string: ")
print_permutations(user_input)

#6
def reverse_words(sentence):
	words = sentence.split()
	reversed_sentence = " ".join(reversed(words))
	return reversed_sentence
userInput = input("Enter a sentence: ")
print(reverse_words(userInput))

#7
def has_33(nums):
	for i in range(len(nums) - 1):
		if nums[i] == 3 and nums[i + 1] == 3:
			return True
	return False
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False

#8
def spy_game(nums):
	code = [0,0,7]
	for num in nums:
		if num == code[0]:
			code.pop(0)
		if not code:
			return True
	return False
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0])) # False

#9
import math
def volume(radius):
	return (4 * math.pi * pow(radius, 3) ) / 3
radius = float(input())
print(volume(radius))

#10
def unique_elements(lst):
	uniquelist = []
	for i in lst:
		if i not in uniquelist:
			uniquelist.append(i)
	return uniquelist
list_numbers = list(map(int, input().split()))
print(unique_elements(list_numbers))

#11
def check_palindrom(s):
	s = s.replace(" ", "").lower()
	return s == s[::-1]
word=str(input())
if(check_palindrom(word)):
	print("Yes")
else:
	print("No")

#12
def histogram(lst):
	for i in lst:
		print( '*' * i)
histogram([4, 9, 7])

#13
import random
def low():
	print("Your guess is too low.")
def high():
	print("Your guess is too high.")

random_number = random.randint(1, 20)

greating = input("Hello! What is your name?\n")
print(f"Well, {greating}, I am thinking of a number between 1 and 20.")
attempts=0
while True:
	guess = int(input("Take a guess\n"))
	attempts+=1
	if guess < random_number:
		low()
	elif guess > random_number:
		high()
	else:
		print(f"Good job, {greating}, You guessed my number in {attempts} guesses")