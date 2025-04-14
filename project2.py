#判断闰年
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)
else:
    print(False)

#身高测算
father_height = int(input())
mother_height = int(input())
gender = input()

if gender == "男":
    height = int((father_height + mother_height) * 1.08 / 2)
    print(height)
elif gender == "女":
    height = int((father_height * 0.923 + mother_height) / 2)
    print(height)
else:
    print("无对应公式")

#百分制成绩转换五分制E
score = int(input())

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score >= 0 and score < 60:
    print("E")
else:
    print("data error!")

#判断是否直角三角形
a = float(input())
b = float(input())
c = float(input())
if a <= 0 or b <= 0 or c <= 0:
    print("NO")
else:
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    if abs(a**2 + b**2 - c**2) < 1e-6:
        print("YES")
    else:
        print("NO")

#分段函数A
x = int(input())

if -10 <= x < 0:
    y = 2 * x**3 + 4 * x**2 + 3
elif 0 <= x < 6:
    y = x + 14
elif 6 <= x <= 10:
    y = 6 * x
else:
    print("ERROR")
    exit()
print(y)