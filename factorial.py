
# import uuid
import time

def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)
try:
    file = open('input_cases.txt', 'r')
except:
    pass
output = open('factorial_output.csv', 'w+')
output.write("RequestID,Time,Number,Result\n")

if file:
    numbers = file.read().splitlines()
    for i, x in enumerate(numbers):
        # unique = uuid.uuid4()
        start = time.time()
        result = factorial(int(x))
        time_taken = time.time() - start
        to_write = str(i) + "," + str(time_taken) + "," + str(x) + "," + str(result) + "\n"
        output.write(to_write)
# print (y_axis_value)
