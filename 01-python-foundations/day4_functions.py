# Functions
from random import shuffle


def say_hello():
    print("Hello how are you?")
    print("how are")
    print(" you?")

say_hello()
print()
def say_hello(name="Jose"):
    print(f"Hello {name}")

say_hello("Aniket")

def add_num(num1,num2):
    return num1+num2

result=add_num(10,20)
print(result)

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

result = return_result(10,20)
print(result)

def myfunc(a,b):
    print(a+b)
    return a+b

result=myfunc(10,30)

def sum_numbers(num1,num2):
    return num1+num2

print(sum_numbers(10,20))
print(sum_numbers('10','20'))

def even_check(num):
    return num%2==0

print(even_check(20))
print()
def check_even_list(num_list):
    even_numbers = []
    for num in num_list:
        if num%2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print(check_even_list([1,3,5]))
print(check_even_list([2,4,5]))
print(check_even_list([2,1,1,1,1]))

# Tuple Unpacking
stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price+(0.1*price))
print()
work_hours=[('Abby',100),('Billy',1400),('Cassie',800)]
def employee_check(work_hours):
    current_max=0
    employee_of_month=""

    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
        else:
            pass
    return employee_of_month,current_max

name,hours = employee_check(work_hours)
print(f"{name} has worked {hours}")

# Three Cup Monte
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

game_list = ['','O','']
shuffle(game_list)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Pick a number 0,1 or 2: ")

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("Correct!!")
    else:
        print("Incorrect!!")
        print(mylist)

def play_game():
    my_list=['','O','']
    mixed_list = shuffle_list(my_list)
    guess = player_guess()

    return check_guess(mixed_list,guess)

print()
# Coding Exercises
#-----------------------------------------
# Functions #1: print Hello World
def hello_world():
    """Function that prints Hello World"""
    print("Hello World")
hello_world()

# Functions 2: print Hello {Name}
def hello_name(name_field="Jose"):
    """Function that prints Hello {name_field}"""

    print(f"Hello {name_field}")
hello_name("Kumar Aniket")

# Functions 3: If z is True return x else return y
def check_z(x,y,z):
    """Function that check the value of z and returns x or y"""
    if z:
        return x
    else:
        return y
z_result = check_z("Hello","Goodbye",False)
print(z_result)
print()
# *args and **kwargs
def myfunc(a,b):
    return sum((a,b)) * 0.05

print(myfunc(40,60))
print()
def myfunc_args(*args):
    return sum(args)*0.05

print(myfunc_args(40,60,100,1,34))

def myfunc_kwargs(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('No fruit')

print(myfunc_kwargs(fruit='apple',veggie='lettuce'))

def myfunc(*args,**kwargs):
    print("I would like {} {}".format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')
print()
def format_server_log(server_name, status_code):
    print("--- Morning Blitz ---")
    print(f"[2026-05-18] SERVER: {server_name} | STATUS: {status_code}")

format_server_log("app-node-1", 200)
