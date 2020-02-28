import random

file = open('input_cases.txt', 'w+')

for i in range(0,100):
    rand_int = random.randint(5,15)
    file.write(str(rand_int) + "\n")
file.close()