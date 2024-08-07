'''
list few methods

'''

## what does it mean when we say 'return type'

# l = [1,2,33,4,5]

# x= l.pop(0)
# print(l)
# print(x)

# x = l.sort()
# print(l)
# print(x)

# x = sorted(l)
# print(l)
# print(x)

# s = sum(l)
# print(s)
# print(l)

# m = max(l)
# print(m)
# mi = min(l)
# print(mi)

# print(max(l))

'''
functions

'''

def myfunc():
    print("hey it is my func")

## calling the fucntion  => () <= calling
# myfunc()


#  fucntion arguments =>a,b
def add(a,b):
    print(a+b)

add(2,5)
add(10,8,2)

# loops, data structures , functions, class , file handling , error handling
mylist = [2,4,6,12,9,13,56,1]
s = sorted(mylist)
print(s)
print(s[:4]) #gives first 4 (4 min)
print(s[len(s)-4:]) #gives last 4(4 max)

def new(s):
    print(s)


def evencnt(l):
    cnt = 0
    for i in l:
        if i % 2==0:
            cnt +=1
    return cnt