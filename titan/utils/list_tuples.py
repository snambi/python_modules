print("hello world")
x = 10
y = []

y.append("hello")
y.insert(1,  "world")

print( y )

def get_name_and_age():
    name = "y"
    age = 24
    
    return name, age

z = [ 3,5,5, 1,0, -9, 34, -3]

print( z )
print( sorted(z) )
print( len(z))

c = get_name_and_age()

print( type(c) )

