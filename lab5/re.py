import re

#1
def mazom(s):
    return bool(re.search(r"ab*", s))

#2
def mattt(s):
    return bool(re.search(r"ab{2,3}", s))

#3
def flu(s):
    return re.findall(r"[a-z]+_[a-z]+", s)

#4
def fufbl(s):
    return re.findall(r"[A-Z][a-z]+", s)

#5
def maab(s):
    return bool(re.fullmatch(r"a.*b", s))

#6
def rwc(s):
    return re.sub(r"[ ,.]", ":", s)

#7
def stc(s):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))

#8
def sau(s):
    return re.split(r"(?=[A-Z])", s)

#9
def iscw(s):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", s)

#10
def cts(s):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", s).lower()


test_strings = [
    "ab", "abb", "abbb", "abc", "A_B", "HelloWorld", "snake_case_string", "ThisIsATest"
]

print("1:", mazom("abbb"))  
print("2:", mattt("abb"))  
print("3:", flu("abc_def ghi_jkl")) 
print("4:", fufbl("Hello World A Test"))  
print("5:", maab("acb"))  
print("6:", rwc("Hello, World. This is a test"))  
print("7:", stc("hello_world_test"))  
print("8:", sau("HelloWorldTest"))  
print("9:", iscw("HelloWorldTest"))  
print("10:", cts("HelloWorldTest")) 
