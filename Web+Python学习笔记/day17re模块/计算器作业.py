import re
#正则表达式 函数 循环
#匹配内层不再有括号的子表达式
#计算
    #先计算乘除法
    #在计算加减法
#一个括号计算完毕
#将结果和括号进行替换
#如何处理符号
#1.先把所有的空格去掉
#    匹配 内层不再有括号的子表达式
#    匹配乘除法
#    匹配加减法
lst=[]
ls=[]
s='1 - 2 * ( (60-30 + (-40/5) * (9-2*5/3 + 7/3*99/4*2998 +10 * 568/14 ))-(-4*3)/ (16-3*2))'
def atom_cal(exp):
    if '*' in exp:
        a,b=exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a,b=exp.split('/')
        return str(float(a) / float(b))
def format_exp(exp):
    exp=exp.replace('--','+')
    exp=exp.replace('-+','-')
    exp=exp.replace('++','+')
    exp=exp.replace('--','-')
    return exp

def cal(exp):
    while True:
        ret=re.search('\d+(\.\d+)?[/*]-?\d+(\.\d+)?',exp)
        print(ret)
        if ret:
            atom=ret.group()
            res=atom_cal(atom)
            exp=exp.replace(atom,res)
        else:
            break
    exp=format_exp(exp)
    print(exp)
    ret=re.findall('[+-]?\d+(?:\.\d+)?',exp)
    num_sum=0
    for i in ret:
        num_sum=float(i)+num_sum
    return num_sum

fun=cal('2-1*-22-3-4/-5')
print(fun)























  
