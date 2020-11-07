
#闭包就是内层函数应用的外层函数的环境变量
# def foo():
#     x = 10
#     def inner():
#         print(x)
#     return inner
#
# print(foo().__closure__[0].cell_contents)

def login(func):
    user = input("user:>>>")
    pwd = input("pwd:>>>")
    def inner():
        if user == 'lyq' and pwd == '123':
            print("成功")
            func()
        else:
            print("失败")

    return inner

@login
def bar():
    print("这是 bar")

bar()
# @login
# def index():
#     print("这是 index")

# func = login(index)
