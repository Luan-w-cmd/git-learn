a=int(input("请输入第一个数字："))
b=input("请输入运算符号：")
c=int(input("请输入第二个数字;"))
if b == "+":
   print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    if c == 0:
        print("除数不能为0")
    else:
        print(a // c)
