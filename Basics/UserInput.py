# # input single variable
# name = input("Enter your name: ")
# print("Hello, " + name + "!")
#
# age = input("Enter your age: ")
# print("You are " + age + " years old.")
#
#
# # input multiple vairable
# # Taking multiple inputs using split()
# values = input("Enter multiple values separated by spaces: ").split()
# print("You entered:", values)
#
# # Taking multiple inputs using list comprehension
# values = [int(x) for x in input("Enter multiple integer values separated by spaces: ").split()]
# print("You entered:", values)


# Make a calculator
num1 = input("Enter number: ") # Python always takes input as strings
num2 = input("Enter number: ")
ans = float(num1) + float(num2)
print(ans)

