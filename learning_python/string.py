'''
strings
are immutable 
'''

s = "sagar teaches ananya "
m = "ananya is a good student"
# s = m
# print(m)
# print(s)
'''
string concatnation
'''
# old = "Hey i am a really amazing programmer"
# new = ""
# for i in old:
#     if i not in "aeiou":
#         new += i    # new = new+i

# print(new)

'''
string methods
'''
# s = "hey hellow"
# print(len(s))

'''
formatted strings or string formating || and join
'''

# join
# l = ["1","2","3"]
# s = "".join(l)
# print(s)

#formatting
myname = "sagar"
age = 23
old_str_for = "hey {} how are u btw you are {} year old".format(age,myname) #python 2
print(old_str_for)

name = input("enter you name: ")
year = int(input("what is your birthyear: "))
age = 2024 - year
s = f"hey {name}, you are {age} year old."
print(s)
