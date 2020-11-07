class Base:
    pass
class Foo(Base):
    pass
class Bar(Foo):
    pass

print(issubclass(Bar,object)) #检查第一个参数是否是第二个参数的子类
  