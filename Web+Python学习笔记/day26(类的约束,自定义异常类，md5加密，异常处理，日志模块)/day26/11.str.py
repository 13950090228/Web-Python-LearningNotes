# by luffycity.com


class Foo:

    def __str__(self):
        return 'asdfadfasdfasd'

obj = Foo()
print(obj,type(obj))

v1 = str(obj)
print(v1)