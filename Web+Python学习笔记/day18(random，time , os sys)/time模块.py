'''
%% %号本身
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
'''
#时间戳 -localtime/gmtime ->结构化时间 -strftime-> 格式化时间(字符串)
#时间戳 <-mktime -结构化时间 <-strptime- 格式化时间(字符串)

import time 
#time.sleep(n)  #程序走到这里睡n秒

#print(time.time())
    #'2018.6.9' 字符串数据类型   格式化时间——给人看的
    #结构化时间
    #1560049546.9941216  浮点数据类型  以秒为单位  时间戳时间——给机器计算用的
    #从 1970.1.1.0:0:0(伦敦时间)

#print(time.strftime('%Y-%m-%d-%r'))
#%Y 年，%m 月，%d 日， %r 当前几时几分几秒 （AM or PM）
    
#时间戳-->结构化时间
#print(time.gmtime(time.time()))    #英国时间
#print(time.localtime(time.time()))  #当地时间

#结构化时间-->时间戳
#time1=time.localtime()
#print(time.mktime(time1))
    
#print(time.localtime())   #结构化时间
#struct_time=time.localtime()
#print(struct_time.tm_mday) 
    
#结构化时间换成字符串时间
struct=time.localtime()
print(struct)
ret=time.strftime('%Y-%m-%d %r',struct)
print(ret)

#字符串时间换成结构化再变成字符串时间
#struct_time=time.strptime('2019-06-09','%Y-%m-%d')
#print(struct_time)
#res=time.mktime(struct_time)
#print(res)

#1、查看一下2000000000时间戳时间表示的年月日
#struct=time.localtime(2000000000)
#res=time.strftime('%Y-%m-%d',struct)
#print(res) 

#2、将2008-8-8转换成时间戳时间
#struct=time.strptime('2008-8-8','%Y-%m-%d')
#print(struct)
#ret=time.mktime(struct)
#print(ret)
#3、请将当前时间的当前月1号的时间戳时间取出来 — 函数

#struct=time.localtime()
#res=time.strptime(str(struct[0])+'-'+str(struct[1])+'-'+'1','%Y-%m-%d')
#print(res)
#ret=time.mktime(res)
#print(ret)
    
#4、计算时间差
    #2018-8-19 22:10:8，2018-8-20 11:07:3
    #经过了多少年月天时分秒
#def time_sub(time1,time2):
#    struct1=time.strptime(time1,'%Y-%m-%d %H:%M:%S')
#    struct2=time.strptime(time2,'%Y-%m-%d %H:%M:%S')
#    time_1=time.mktime(struct1)
#    time_2=time.mktime(struct2)
#    sub=time_2-time_1
#    gm_time=time.gmtime(sub) # 将时间戳转换为格式化
#    print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(gm_time.tm_year-1970,gm_time.tm_mon-1,
#                                           gm_time.tm_mday-1,gm_time.tm_hour,
#                                           gm_time.tm_min,gm_time.tm_sec))
#time_sub(time1='2010-8-19 10:10:8',time2='2018-8-20 1:07:5')
#    
#
#struct1=time.strptime('2010-8-19 10:10:8','%Y-%m-%d %H:%M:%S')
#struct2=time .strptime('2018-8-20 1:07:5','%Y-%m-%d %H:%M:%S')
#ret1=time.mktime(struct1)
#ret2=time.mktime(struct2)
#sub=ret2-ret1
#gm=time.gmtime(sub)
#
#print('过去了%d年 %d月 %d日 %d时 %d分 %d秒'%(gm.tm_year-1970,gm.tm_mon-1,gm.tm_mday-1,gm.tm_hour,gm.tm_min,gm.tm_sec))
#








