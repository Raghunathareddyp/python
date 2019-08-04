from sys import argv
script_name = argv[0]
arguments = argv[1:]
count = len(arguments)
print(f'{script_name} has {count} arguments')

def myFun(*args,**kwargs): 
	print("arg1:", kwargs[0]) 
	print("arg2:", kwargs[1]) 
	print("arg3:", kwargs[2]) 
	
# Now we can use *args or **kwargs to 
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks","hello") 
myFun(*args) 

#kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks","arg4":"Hello"} 
#myFun(**kwargs) 

