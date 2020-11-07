import random as r
def sendred(money,n):
    money=money*100
    ret=r.sample(range(1,money),n-1)
    ret.sort()
    ret.insert(0,0)
    ret.append(money)
    for i in range(len(ret)-1):
        yield (ret[i+1]-ret[i])/100

ret_g= sendred(200,10)
for money in ret_g:
    print(money)