__author__ = 'oucb'

class Foo(object):
    pass

class Foo1:
    pass

print type(Foo), type(Foo1)
print dir(Foo)
print dir(Foo1)

print isinstance(Foo, object)
print isinstance(Foo1, object)
