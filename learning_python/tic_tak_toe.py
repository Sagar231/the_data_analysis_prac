'''
tic_tak_toe

'''

# greeting the player
print("Hello! players here is the classic tic tak toe empty board\n")
mylist = [[". ",". ",". "],[". ",". ",". "],[". ",". ",". "]]

# printing the board
for row in mylist:
    for ele in row:
        print(ele,end=" ")
    print("\n")

# creating a dictionary which gives the row and col according to the user input
pos = {
    1:[0,0],2:[0,1],3:[0,2],
    4:[1,0],5:[1,1],6:[1,2],
    7:[2,0],8:[2,1],9:[2,2]
}

flag = False #defining the initial flag for the charachter change

#the game
while(True):
    
    #take the input with error handling
    try:
       position = int(input("hey player choose an input from 1 to 9: "))
    except:
        print("Wrong input, please enter an integer")
        continue
    if position <1 or position > 9:
        print("Please give value in range 1 to 9")
        continue
    
    # choose the character according to the flag
    if flag == False:
        character = "0 "
    if flag ==  True:
        character = "x "
    
    # get the position according to the input
    r,c = pos[position]
    if mylist[r][c] != ". ": # check if it is already filled with some character
        print("This position is taken, please give another ")
        continue
    mylist[r][c] = character # put the character (make you move in game)
    
    #print the board
    for row in mylist:
        for ele in row:
            print(ele,end=" ")
        print("\n")
    
    # toggle the flag to change the character in next term
    flag = not flag