#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    l = "My String"
    add_attribute(l, "name", "Bob")
    print(l.name)
except Exception as m:
    print("[{}] {}".format(m.__class__.__name__, m))
