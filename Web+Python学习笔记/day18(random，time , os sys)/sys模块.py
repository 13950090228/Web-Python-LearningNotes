#sys 是和 python解释器打交道
#sys.argv
import sys
#sys.argv
#user=sys.argv[1]
#pwd=sys.argv[2]
#if user == 'alex' and pwd == 'alex123':
#    print('登陆成功')
#else:
#    exit()
#1.一般都是在命令行运行代码
#2.操作系统若处于input，则会发生阻塞，退出CPU竞争

#sys.path
#print(sys.path)
#模块应该是存在硬盘上
#但是再使用import的时候，这个模块才到内存中
#一个模块能否被顺利的导入，全看sys.path 下面有没有这个模块所在的
#sys.modules
#print(sys.modules['re'])
print(sys.path)