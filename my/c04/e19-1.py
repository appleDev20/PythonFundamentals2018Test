# e19-1
# Initialise global variable "number" to 5
number = 5


def summation(first, second):
    # Add the parameters and global number together
    total = first + second + number
    # Return result
    return total


# Call the "summation" function with two parameters as excepted
# Assign the result of "summation" to the variable "outer_total"
outer_total = summation(10, 20)
# Print out the initial value of "number"
print("The first number we initialised was " + str(number))
# Try to access the local variable "total"
print("The total after summation is " + str(outer_total))
