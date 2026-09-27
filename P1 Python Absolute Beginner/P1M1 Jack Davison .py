# Create name check code
print("Jack Davison")
# [ ] get input for input_test variable
input_test = input("Names of people met in the last 24 hours: ").lower()
# [ ] print "True" message if "John" is in the input or False message if not
print("john" in input_test)

# [ ] print True message if your name is in the input or False if not
my_name = input("Enter your name: ").lower()
print(my_name in input_test)

# [ ] Challenge: Check if another person's name is in the input - print message
print("Timmy" in input_test)

# [ ] Challenge: Check if a fourth person's name is in the input - print message
print("Sally" in input_test)