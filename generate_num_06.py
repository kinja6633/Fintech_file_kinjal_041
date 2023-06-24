# Python program to generate a random number
import random

# using random function
a = random.random()
print(a)

#using randint function
b = random.randint(1,10)
print(b)

# using for loop
rand_list = []
for i in range(0,10):
    n = random.randint(1,50)
    rand_list.append(n)
print(rand_list)