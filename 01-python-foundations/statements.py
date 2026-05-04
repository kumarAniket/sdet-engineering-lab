from random import shuffle,randint

# If,Elif & Else Statements
print("----- If,Elif & Else -----")
hungry = False
if hungry:
    print('Feed me!!')
else:
    print("I'm already full!!")
print()
loc = "Bank2"

if loc == "Auto Shop":
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Game":
    print("Game is on!!!")
else:
    print("I do no know much!!")
print()
print("----- For Loops -----")
# For Loops
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print("Hello")
print()
for num in mylist:
    if num%2 == 0:
        print(f'Even number {num}')
    else:
        print(f'Odd number {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)
print()
my_string = "Hello World"
for letter in my_string:
    print(letter)
print()
print("----- While Loops -----")
x=5
while x<5:
    print(f'The current value of x is {x}')
    x+=1
else:
    print("x is not less than 5")
print()
print("----- Additional Functionality -----")
#break, continue & pass

x=[1,2,3]
for item in x:
    pass

my_string = "Sammy"
for letter in my_string:
    if letter == "a":
        continue
    print(letter)
print()
for letter in my_string:
    if letter == "a":
        break
    print(letter)
print()
for letter in my_string:
    if letter == "a":
        pass
    print(letter)

x=0
while x<5:
    x+=1
    if x==2:
        break
    print(x)
print()
print("--- Useful Operators ---")
print()
print("--- Range ---")
# Range Operator
for x in range(0,10,2):
    print(x)
print()
print("--- Enumerate ---")
# Enumerate Operator
word = "abcde"
for item in enumerate(word):
    print(item)
print()
print("--- Shuffle ---")
# Shuffle function
mylist = [1,2,3,4,5]
shuffle(mylist)
print(mylist)
# Random Integer
print()
print("--- Random Integer ---")
random_choice = randint(0,125)
print("Random Number: {}".format(random_choice))

mylist = [x*y for x in range(2,7,2) for y in range(1,100,50)]
print(mylist)
