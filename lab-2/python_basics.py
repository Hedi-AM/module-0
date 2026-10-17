import copy

# 1. Basic Data Types & Strings
print("--- 1. Data Types ---")
print(True + False)  # Output: 1[cite: 25]
S = 'python'
print(len(S))         # Output: 6[cite: 26]
print(S[0], S[1], S[-1]) # Output: p y n[cite: 26]

# 2. Deep Copy vs Shallow Copy
print("\n--- 2. Deep vs Shallow Copy ---")
Dict1 = {'name': 'lee', 'age': 89, 'num': [1, 2, 8]}
Dict_copy = Dict1.copy()         # Shallow copy[cite: 29]
Dict_dcopy = copy.deepcopy(Dict1) # Deep copy[cite: 29]
Dict1['num'][1] = 6
print("Dict1:", Dict1)
print("Dict_copy (affected):", Dict_copy)
print("Dict_dcopy (safe):", Dict_dcopy)

# 3. Flow Control & Exception Handling
print("\n--- 3. Exception Handling ---")
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Error: The second digit cannot be 0.")[cite: 35]

# 4. Custom Functions
print("\n--- 4. Custom Functions ---")
def hello(greeting='hello', name='world'):
    return f"{greeting}, {name}!"

print(hello())                  # hello, world![cite: 32]
print(hello('Greetings', 'universe')) # Greetings, universe![cite: 32]

# 5. Object-Oriented Programming (Classes & Inheritance)
print("\n--- 5. OOP (Dog Class) ---")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Private attribute[cite: 37]

    def sit(self):
        print(f"{self.name} is now sitting.")[cite: 37]

class Husky(Dog):
    def shout(self):
        print("Woo!")[cite: 38]

# Instantiate objects
my_dog = Husky("Larry", 3)
my_dog.sit()
my_dog.shout()
