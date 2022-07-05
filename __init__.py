







exit()
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")

j = planets[-1]
print(j)
print("Jupiter is the", jupiter_index + 1, "th planet from the sun")
print("Jupiter" + str(jupiter_index))


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

type_check = isinstance(fact_split, str)
print(type_check)