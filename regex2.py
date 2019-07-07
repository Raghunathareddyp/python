import re
pattern = r"[\t ]+"
obj = re.compile(pattern)
print(obj)
text= "live and let \t \tlive"
print(obj.sub(" ",text))