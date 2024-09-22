# strings are immutable means cannot change,but a new string can form using string methods.
a="!!!!Harry !!!!!!!  Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))       
# strip the trailing chracters
print(a.replace("Harry","john"))
# replace is use for replacing strings with the new word
print(a.split(" "))
# split is use for spliting the string in list.
blogheading="introduction to js"
print(blogheading.capitalize())
# for capitaling only first letter of string but change all other chracters in lowercase
str1="welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
# centre method alligns the string to the centre
print(a.count("Harry"))
# count method returns the number of times the given value ocurre within the string
str1="welcome to the console!!!"
print(str1.endswith("!!!"))
str1="welcome to the console!!!"
print(str1.endswith("to",4,10))
# endswith method is use to checks the string ends with the given value ,if yes then returns true.
str1="he's name is dan.he is an honest man"
print(str1.find("is"))
# find method is use to find the occurence of given value and return its index it returns the index of first value.
# and if the value is not present it returns -1.but index method raise an exception and return an error.
print(str1.find("issh"))
# print(str1.index("issh"))
print(str1.isalnum())
# isalnum is use to see the string is alphanumeric or not
str1="welcome00\n"
print(str1.isalpha())
# isalpha is use to see only alphabets in string
print(str1.islower())
print(str1.isprintable())
# isprintable is use to see if the all chracters are printable or not
print(str1.isspace())
str1="World Health orgnization"
print(str1.istitle())
# istitle method is use to check if first letter of each wors is capital or not.
str1="python is an interpreted language"
print(str1.startswith("python"))
print(str1.swapcase())
# swapcase is use to swap the uppercase letters to lower case and lowercase letters to upper case.
print(str1.title())
# title method is sus to change the words in title case means first letter of each wors is capital.


                        