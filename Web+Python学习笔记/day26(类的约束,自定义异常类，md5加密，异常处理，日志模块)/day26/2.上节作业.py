# by luffycity.com



class Course:
    def __init__ (self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
class Student:

    func_list = [
        {'text':'选课','name':'select_course'},
        {'text':'查看课程','name':'show_selected_course'},
        {'text':'删除课程','name':'show_del_course'},
    ]

    def __init__ (self,name):
        self.name = name
        self.courses = []
    def select_course(self,csl):
        pass
    def show_selected_course(self,csl):
        pass
    def show_del_course(self,csl):
        pass

def run():
    total_course_list = []
    for i in range(1,11):
        obj = Course('xx-%s' % i, 90, 90)
        total_course_list.append(obj)

    stu_name = input('请输入学生姓名')
    stu = Student(stu_name)

    for i,item in enumerate(stu.func_list,1):
        print(i,item['text'])


    while True:
        num = int(input('请选择要执行的功能序号：'))
        num = num-1
        row = stu.func_list[num]
        name = row['name']
        func = getattr(stu,name)
        func(total_course_list)

if __name__ == '__main__':
    run()