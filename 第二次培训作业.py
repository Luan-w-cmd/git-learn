#作业一
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def average_score(self):
        return sum(self.score)/len(self.score)
stu_1 = Student("张三",18,[90,80,95])
stu_2 = Student("李四",19,[98,80,90])
average1 = stu_1.average_score()
average2 = stu_2.average_score()
print(stu_1.name,stu_1.age,stu_1.score)
print(stu_2.name,stu_2.age,stu_2.score)
print("张三的平均成绩为：",average1)
print("李四的平均成绩为:",average2)

#作业二
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
ele = tuple[-1]
#ele是什么
print(ele)
#ele表示这个元组的最后一个元素
ele2 = tuple[-2]
print(ele2)

#动物类
class animal:
    def 叫(self):
        print("某种动物在叫")
class dog(animal):
    def 叫(self):
        print("旺旺！")
class cat(animal):
    def 叫(self):
        print("喵喵！")
dog = dog()
cat = cat()

dog.叫()
cat.叫()




