def add(a,b):
    print(f"i am going to add {a} and {b}")
    return a+b

def sub(a,b):
    print(f'i am going to minus {a} with {b} ')
    return a-b

def mul(a,b):
    print(f'i am going to multiply {a} with {b}')
    return a*b

def div(a,b):
    print(f'i am going to division {a} with {b}')
    return a/b

print('lets do some math with just functions')

age = add(30, 1)
print(age)
height = sub(100, 67)
print(height)
weight = mul(31, 2)
print(weight)
iq = div(100, 2)
print(iq)
print(f'Age: {age}, Height: {height}, Weight: {weight}, iq: {iq}')

print("Here is a puzzle.")

what = add(age, sub(height, mul(weight, div(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

what = mul(age, div(height, add(weight, sub(iq, 10))))

print("That becomes: ", what, "Can you do it by hand?")