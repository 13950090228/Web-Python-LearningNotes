#有序数列才能使用二分法
#lst=[]
#for i in range(1,100000000):
#    lst.append(i)
##lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,45,56]
#n=10
#left=0
#right=len(lst)-1
#
#while left<=right:
#    mid=(left+right)//2
#    if lst[mid]>n:
#        right=mid-1
#    elif lst[mid]<n:
#        left=mid+1
#    elif lst[mid]==n:
#        print('找到了')
#        
#        break
#else:
#    print('没找到')
#s='isghapodhgopqwejhpoqehgoqwgoasdhq'
#dic={}
#for i in s:
#    if dic.get(i)==None:
#        dic[i]=1
#    else:
#        dic[i]=dic[i]+1
#print(dic)


#递归完成二分法
#lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,45,56]
#def fun(n,left,right):
#    mid=(left+right)//2
#    if left<=right:
#        if n>lst[mid]:
#            left=mid+1
#            return fun(n,left,right)
#        if n<lst[mid]:
#            right=mid-1
#            #深坑，函数的返回值返回给调用者
#            return fun(n,left,right)
#        if n==lst[mid]:
#            print('找到了')
#            return mid
#    else:
#        print('找不到')
#        return -1
#    
#
#print(fun(10,0,len(lst)-1))

#最快查找
#时间复杂度最低，空间复杂度最低
lst1=[5,6,7,8,9]
lst2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
for i in lst1:
    lst2[i]=1

lst2[5]==1











