dic={'key1':'你好','key2':'2','key3':3,'key4':4}
dic1={'key3':3,'key4':4}
import json
#ret=json.dumps(dic,ensure_ascii=False,separators={',',':'},indent=2)
#print(ret)
#print(ret)
#ret=json.dumps(dic)  #dumps 序列化
#print(dic,type(dic))
#print(ret,type(ret))
#
#res=json.loads(ret)  #loads 反序列化
#print(res,type(res))

#json  在所有的语言中都通用：json序列化的数据 在python上序列化可以在别的语言中反序列化
#能够处理的数据类型非常有限：字符串 列表 字典 数字
#字典中的key只能是字符串

#向文件中记录字典
#with open('json_file','a') as f:
#    print(ret)
#    f.write(ret)
#f.close()

#向文件中读取字典
#with open('json_file','r') as f:
#    file=f.read()
#print(json.loads(file))
#f.close()


#load dump  #不支持连续的读
#with open('json_file','a') as f:
#    json.dump(dic,f)
#    json.dump(dic1,f)
#f.close()

#多行写入多行读方法

with open('json_file','r') as f:
    for i in f:
        dic1=json.loads(i.strip())
        print(dic1)

f.close()


#
#ret=json.dumps(dic)
#with open('json_file','a') as f:
#    for i in range(3):
#        f.write(ret+'\n')
#f.close()

# dumps loads 
    #在内存中做数据转换：
        #dumps 将 数据类型 转为 字符串    序列化
        #loads 将 字符串 转为 数据类型  反序列化
    
# dump load
    #直接将数据类型写入文件，从文件中读出数据类型：
        #dump 数据类型 写入 文件   序列化
        #load 文件 读书 数据类型  反序列化
    












