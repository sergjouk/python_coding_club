
fact = "something and something else"

#import sys
#print(sys.argv[1])

fact_split = fact.split(" ")

print(fact_split)
for item in fact_split:
    print(item)

some_list = ['a','b']
print(some_list[1])

def some_method(name):
    print(str(name) +" a method")

some_method("SSS")
exit()
type_check = isinstance(fact_split, str)
print(type_check)