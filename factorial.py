
# import uuid
import time
import matplotlib.pyplot as plt

def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)
try:
    file = open('input_cases.txt', 'r')
except:
    pass

x_axis_value = []
y_axis_value = []
if file:
    numbers = file.read().splitlines()
    for i, x in enumerate(numbers):
        # unique = uuid.uuid4()
        start = time.time()
        factorial(int(x))
        time_taken = time.time() - start
        y_axis_value.append(time_taken)
        x_axis_value.append(str(i))
# print (y_axis_value)
plt.xticks([x*10 for x in range(0,10)])
plt.xlabel("Request ID")
plt.ylabel("Time")
plt.plot(x_axis_value, y_axis_value, color='red')
plt.savefig("factorial.png")