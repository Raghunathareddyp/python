''' cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_car
avg_passengers_per_car = passengers / cars_driven

print("There are ", cars , "cars available")
print("there are only" , drivers , " drivers available")
print("there will be " , cars_not_driven , " empty cars today")
print("we can transport " , car_pool_capacity , " people today")
print("we have ", passengers , "to car pool today")
print("we need to put about",  avg_passengers_per_car , " in each car") '''

my_name = 'Zed A. Shaw'
my_age = 30 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eys = 'blue'
my_teeth = 'white'
my_hair = 'Brown'

print(f"let's talk about {my_name} .")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy")
print("that's actually not heavy")
print(f"He's got {my_eys} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending ont the coffe" )

# this line is tricky

total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_weight}, and {my_height} I get {total}")