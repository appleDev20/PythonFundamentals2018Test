#
# Loop over all numbers from 1 to 10
for number in range(1, 11):
    # If the number is 4, exit the loop
    if number == 4:
        break

    # Calculate the product of number and 2
    product = number * 2
    # Print out the product in a friendly way
    print(number, '* 2 = ', product)

print('Loop completed')

