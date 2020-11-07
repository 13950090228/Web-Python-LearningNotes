class fun:
    def __init__(self,lst,pag,num=10):
        self.pag=pag
        self.num=num
        self.lst=lst
    @property
    def start(self):
        return (self.pag-1)*self.num

    @property
    def end(self):
        return (self.pag-1)*self.num+self.num

    def show(self):
        result= self.lst[(self.pag-1)*self.num:(self.pag-1)*self.num+self.num]
        for i in result:
            print(i)
        
lst=[]
for i in range(1,901):
    lst.append('鸡巴-%s'%i)
while True:
    try:
        num=10
        pag=int(input('输入你要查看的页码：'))
        obj=fun(lst,pag,num)
        print(obj.show())
    except ValueError:
        print('请输入数字！！')
        break