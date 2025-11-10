while True:
    try:
        a=int(input("请输入第一个数字："))
    except ValueError:
        print("请输入整数")
        continue

    b=input("请输入运算符号：")

    try:
        c=int(input("请输入第二个数字："))
    except ValueError:
        print("请输入整数")
        continue
        
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
    else:
          print("运算符号错误，请输入+,-,*,/")

    continue_choice = input("\n是否继续？(输入'y'继续，其他键退出)：")
    if continue_choice.lower() != "y":
        break

