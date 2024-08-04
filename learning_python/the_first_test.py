'''
Question: Count Vowels in a String

Write a Python function that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.
'''
def func(s):
    cnt = 0  
    for i in s:
        if i in "aeiou":
            cnt+=1
    return cnt

'''
Question: Sum of Even Numbers in a List

Write a Python function that takes a list of integers as input and returns the sum of all even numbers in the list.
'''
def count_even(l):
    s = 0
    for i in l:
        if i%2==0:
            s += i
    return s
# mylist = list(map(int , input("give me numbers with space: ").split()))
# print(count_even(mylist))


'''
Question: Merge Two Dictionaries

Write a Python function that takes two dictionaries as input and returns a new dictionary that contains all the key-value pairs from both dictionaries. If a key is present in both dictionaries, the value from the second dictionary should be used.
{"hey": "there","no" : "problem"},{"name":"anaa" , "friend" : "jass"}
'''
def dict_func(d1, d2):
    new_dict = dict()
    for key in d1.keys():
        new_dict[key] = d1[key]
        
    for key in d2.keys():
        new_dict[key] = d2[key]
        
    return new_dict
first_dict = {"hey": "there","no" : "problem"}
sec_dict = {"name":"anaa" , "friend" : "jass"}
print(dict_func(first_dict, sec_dict))


'''
Question: Group Strings by Length

Write a Python function that takes a list of strings as input and returns a dictionary where the keys are lengths of strings, and the values are lists of strings of that length.
'''

mylist = ["sagar","is","a","good","guy"]
d = {
    5 : ["s","a","g","a","r"],
    2 : ["i","s"]
}
def func_new(l):
    d = dict()
    for element in l:
        key = len(element)
        value = []
        for i in element:
            value.append(i)
        d[key] = value
    return d
print(func_new(mylist))