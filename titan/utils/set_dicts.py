a = {3,4,5,6,6}
b = set({1,1,1,1,2,3,5,6,7,8})

print(f"set a {a} and set b {b}" )
print("set a %s and set b %s" % (a, b) )

x = a.difference(b)
print( f"diff {x}")

x = a.symmetric_difference(b)
print( f"sym diff {x}")


x = a.union(b)
print( f"union {x} len {len(x)}")

x = a.intersection(b)
print( f"intersection {x}", end="\n!")

import list_tuples

print(list_tuples.get_name_and_age())

if __name__ == "__main__":
    print("executing mains")