#作业一
m = 66
left = 0
right = 100
for i in range(100):
    mid = (left + right) / 2
    print(mid)
    if mid == m:
        print(i+1)
        break
    elif mid < m:
        left = mid
    elif mid > m:
        right = mid

#作业二
#列表的查询
lst = [1,2,3,4,5,6,7,8,9]
print(lst[3])

#列表的修改
lst[5] = 66
print(lst)

#列表的插入
lst.insert(0,1)
print(lst)

#列表的删除
lst.remove(9)
print(lst)

#列表的添加
lst.append(10)
print(lst)

#查询列表的下标
tup = (1,2,2,"helo")
print(tup[1])
#统计出现次数
print(tup.count(2))

#字典的添加
dic = {"张三":98,"李四":89,"李华":60}
dic["王五"]=89
print(dic)

#字典的修改
dic["李四"] = 100
print(dic)

#字典的删除
del dic["张三"]
print(dic)

#遍历字典
for name,score in dic.items():
    print(name,score)

#列表的交集和并集
lst1 = [1,2,3,4]
lst2 = [4,5,6,7]
print(set(lst1) & set(lst2))
print(set(lst1) | set(lst2))

