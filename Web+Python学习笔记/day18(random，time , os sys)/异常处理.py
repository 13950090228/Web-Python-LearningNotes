l=['login','register']
#for num,i in enumerate(l,1):
#    print(num,i)

#单分支结构
#try:
#    num=int(input('num>>'))
#    print(l[num-1])
#except ValueError:   #except处理的异常必须和实际报错的异常相同
#    print('请输入数字!!')
    
##多分支
#try:
#    num=int(input('num>>'))
#    print(l[num-1])
#except ValueError:   #从上向下报错的代码只要找到一个和报错相符就执行这个分支的代码，然后退出。
#    print('请输入数字！！')
#except IndexError:
#    print('只能输入1和2')

#多分支合并
#try:
#    num=int(input('num>>'))
#    print(l[num-1])
#except (ValueError,IndexError):   #except处理的异常必须和实际报错的异常相同
#    print('您的输入不合法')

#万能异常应该永远放在最下面
#def buy():
#    print('buy')
#    name
#
#def back():
#    print('back')
#    [][1]
#
#def show():
#    print('show')
#    1/0
#
#def main():
#    l=[('购物',buy),('退货',back),('查看订单',show)]
#    while True:
#        for num,i in enumerate(l,1):
#            print(num,i)
#        try:
#            num=int(input('num>>>'))
#            print(l[num-1])
#        
#            func = l[num-1][1]
#            func()
#        except (ValueError,IndexError):   #except处理的异常必须和实际报错的异常相同
#            print('您的输入不合法')
#        except Exception as e:
#            print(e.args,e.__traceback__.tb_lineno,e.__traceback__.tb_frame)
#            print('用户在选择了%s操作之后发生了不可知的异常' %l[num-1][0])
#main()
        
#else分支
#try:
#    print('aaa')
##    name
##    [][1]
##    1/0
#except NameError:
#    print('name error')
#except IndexError:
#    print('index error')
#else:         #当try中的代码不发生异常时，走else分支
#    print('bbb')

#finally分支
#try:
#    print('aaa')
##    name
##    [][1]
##    1/0
#except NameError:
#    print('name error')
#except IndexError:
#    print('index error')
#finally:    #例如打开文件进行操作，不管报不报错，都要执行close，所以使用finally
#    print('finally')

#主动抛异常:是给其他开发者用的
#raise ValueError('你写的不对')
#django是别人写的程序 框架-->程序员用

#断言 - 语法：正确就继续执行，错误就抛异常
#assert 1==2 #只能接受一个布尔值  False
#assert 1==1 #只能接受一个布尔值  True
#print('aaaaa')

#类似
#if 1==int(input()):
#    pass
#else:
#    raise ValueError
    
#自定义异常：面向对象之后
#异常处理的忠告：在最外层的异常处理应该在










        
        
        
        
        