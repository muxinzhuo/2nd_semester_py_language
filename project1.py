###### Begin ######
print("Hello Python")
###### End ######

# Begin
name = input("请输入一个人的名字：")
country = input("请输入一个国家的名字：")
print("世界那么大，{}想去{}看看。".format(name, country))
# End

# Begin
name=input("输入姓名：")
print("{}同学，学好Python，前途无量！".format(name))
print("{}大侠，学好Python，大展拳脚！".format(name[0]))
print("{}哥哥，学好Python，人见人爱！".format(name[1:]))
# End

#表达式求值
import math
# 从输入中读取a, b, c的值
a = float(input())
b = float(input())
c = float(input())
# 检查根号下的值是否大于或等于0
if b**2 - 4*a*c < 0:
    print("根号下的值小于0，无法计算实数解。")
else:
    # 计算x的值
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    
    # 输出结果，保留两位小数
    print(f"{x:.2f}")

#三角形周长与面积
import math
# 从输入中读取三角形的三条边长
a = float(input())
b = float(input())
c = float(input())
# 计算周长
perimeter = a + b + c
# 计算半周长
s = perimeter / 2
# 计算面积
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# 输出结果，保留两位小数
print(f"周长={perimeter:.2f}")
print(f"面积={area:.2f}")

#幂运算
a = int(input())
b = int(input())
m = int(input())
print(pow(a, b))
print(pow(a, b, m))

#整数四则运算
A = int(input())
B = int(input())
print(f"{A} + {B} = {A + B}")
print(f"{A} - {B} = {A - B}")
print(f"{A} * {B} = {A * B}")
print(f"{A} / {B} = {A / B}")

#求绝对值
n = input()
if '.' in n:
    n = float(n)
    print(abs(n))
else:
    n = int(n)
    print(abs(n))

#数制转换
n = int(input())
if n < 0:
    print(f"-0o{oct(-n)[2:]}")
    print(f"-0x{hex(-n)[2:]}")
else:
    print(f"0o{oct(n)[2:]}")
    print(f"0x{hex(n)[2:]}")

#计算矩形面积
a = eval(input())
b = eval(input())
print(a * b)

#浮点数四则运算与格式化输出
num1 = float(input())
num2 = float(input())
print(f"{num1} + {num2} = {num1 + num2:.3f}")
print(f"{num1} - {num2} = {num1 - num2:.3f}")
print(f"{num1} * {num2} = {num1 * num2:.3f}")
print(f"{num1} / {num2} = {num1 / num2:.3f}")

#计算矩形面积
a = eval(input())
b = eval(input())
print(a * b)

#自我介绍
name = input()
city = input()
hobby = input()
print(f"我的名字是{name}，来自{city}，我的爱好是{hobby}！")

#控制小数输出精度
num = float(input())
print(f"{num:.3f}")

#整数A+B
num1 = int(input())
num2 = int(input())
print(num1 + num2)

#字符串输出
print("眼过千遍不如手过一遍！")
print("书看千行不如手敲一行！")

#你好，中国！
print("你好，中国！")
