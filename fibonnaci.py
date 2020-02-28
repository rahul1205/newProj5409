
# import uuid
import time
import matplotlib.pyplot as plt

def fibonacci(number): 
    if number <= 1:
       return number
    else:
       return(fibonacci(number-1) + fibonacci(number-2))

# output_str =    ""
# for i in range(int(5)):

#     output_str += str(fibonacci(i)) + "|"
# print (output_str)


try:
    file = open('input_cases.txt', 'r')
except:
    pass
output = open('fibonnaci_output.csv', 'w+')
output.write("RequestID,Time,Number,Result\n")
if file:
    numbers = file.read().splitlines()
    for i, x in enumerate(numbers):
        # unique = uuid.uuid4()
        start = time.time()
        output_str =    ""
        for i in range(int(x)):
            output_str += str(fibonacci(i)) + "#"
        time_taken = time.time() - start
        to_write = str(i) + "," + str(time_taken) + "," + str(x) + "," + str(output_str.rstrip("|")) + "\n"
        print (to_write.rstrip("|"))
        output.write(to_write)


