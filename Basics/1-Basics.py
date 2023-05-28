from math import *
###### VARIABLE
#No need to mention dataTyype
age = 50
name = "Zihad"

### Strings
print("Giraffe Academy")
print("Giraffe\n Academy")
phrase = "Giraffe Academy"
print(phrase + " is cool")
print((phrase.upper()))
print((phrase.lower().isupper())) #check is upper
print(len(phrase))

# index
print((phrase.index("G")))
print(phrase.index("Aca")) # where "Aca" starts

# string functions
print(phrase.replace("Giraffe", "Elephant")) # prints Elephant academy
print((phrase)) # prints GIraffe Academy, means replace() function doesn't totally change the string

print(phrase.find('Ac'))
print(phrase.count("a"))


### Numbers
num = 5
print(str(num) + " is my number") #need to convert num to string to print it with strings
print(pow(4, 5)) #pow(number, power)
print(round(5.4))
print(round(5.6))
print(floor(4.5))












