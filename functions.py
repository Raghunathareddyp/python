''' 
def print_two(*args):
    arg1,arg2=args
    print(f'argument 1 : {arg1} , argument 2 : {arg2}')

def print_two_again(arg1 , arg2):
    print(f'argument 1 : {arg1} , argument 2: {arg2}')

def print_one(arg1):
    print(f'only one argument: {arg1}')

def print_nothing():
    print(f'nothing to print')

print_two("abc","efg")
print_two_again("xyz","klm")
print_one("hello")
print_nothing() 

'''

def print_two(*argv):
    arg1,arg2=argv
    print(f'argument 1 : {arg1} , argument 2 : {arg2}')

def print_two_again(arg1 , arg2):
    print(f'argument 1 : {arg1} , argument 2: {arg2}')

def print_one(arg1):
    print(f'only one argument: {arg1}')

def print_nothing():
    print(f'nothing to print')

print_two("abc","efg")
print_two_again("xyz","klm")
print_one("hello")
print_nothing()