def say_hi(name, age):
    return "Hello " + name + ". You are " + str(age)


print(say_hi("Zihad", 24))


# Default Parameters:
def sayHi(name="Soyaib", age=10):  # name = "Soyaib" is default parameter
    return "Hello " + name + ". You are " + str(age)


print(sayHi("Zihad", 24))
print(sayHi())  # no parameter provided so defaults gets counted.


# Variable Number of Arguments:
def fruit(*p):
    for i in p: print(i)


print("apple", "lichi", "strawberry")


# Variable Number of Arguments:
def greet(last_name, first_name):
    print("Hello,", first_name, last_name)


greet(first_name="Alice", last_name="Smith")  # here we specify fist_name, last_name. So, it doesn't matter which order names are in the pareameter
