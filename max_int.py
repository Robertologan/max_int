num_int = int(input("Input a number: "))    # Do not change this line

numbers =  100000 # putting a high number so it covers the input
max_int = float("-inf") # the max int is a float number is infinite + numbers

for i in range(numbers):  # finding a number in this range 
    

    number = int(input("Input a number: "))
    if number > max_int:
        max_int = number
    elif number <0:
        break



print("The maximum is", max_int)    # Do not change this line




