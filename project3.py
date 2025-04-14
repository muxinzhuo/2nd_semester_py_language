#猜数游戏
import random
random.seed(int(input()))
target = random.randint(1, 1024)
guess_count = 0
max_guesses = 10

while guess_count < max_guesses:
    guess = int(input())
    guess_count += 1

    if guess < target:
        print("猜的数小了")
    elif guess > target:
        print("猜的数大了")
    else:
        print(f"恭喜你仅用了{guess_count}次就猜到这个数字是{target}")
        break
else:
    print("你没猜中哦")

#超市收银小程序
amount_due = float(input())
amount_paid = float(input())

change = amount_paid - amount_due

print(f"需支付的金额：{amount_due:.2f}元")
print(f"实际支付的金额：{amount_paid:.2f}元")
print(f"找零金额为：{change:.2f}元")

change_in_fen = round(change * 100)

denominations = [
    (5000, "50元纸币数量为：", "张"),
    (2000, "20元纸币数量为：", "张"),
    (1000, "10元纸币数量为：", "张"),
    (500, "5元纸币数量为：", "张"),
    (200, "2元纸币数量为：", "张"),
    (100, "1元纸币数量为：", "张"),
    (50, "5角硬币数量为：", "个"),
    (20, "2角硬币数量为：", "个"),
    (10, "1角硬币数量为：", "个"),
    (5, "5分硬币数量为：", "个"),
    (2, "2分硬币数量为：", "个"),
    (1, "1分硬币数量为：", "个")
]

for denom in denominations:
    value, text, unit = denom
    count = change_in_fen // value
    if count > 0:
        print(f"{text}{count}{unit}")
        change_in_fen -= count * value

#判断运算结果的奇偶
n = int(input())
sum_squares = n * (n + 1) * (2 * n + 1) // 6
if sum_squares % 2 == 0:
    print("偶数")
else:
    print("奇数")

#输出N以内的所有素数
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def output_prime(number):
    for num in range(2, number + 1):
        if is_prime(num):
            print(num, end=' ')

positive_int = int(input())  
output_prime(positive_int)

#出租车计费
distance, wait_time = map(int, input().split(','))
fare = 0

if distance <= 3:
    fare = 13
elif 3 < distance <= 15:
    fare = 13 + 2.3 * (distance - 3)
else:
    fare = 13 + 2.3 * 12 + 3.45 * (distance - 15)

fare += wait_time * 1
print(int(fare))

#计算圆周率
def leibniz_of_pi(error):
    """接收用户输入的浮点数阈值为参数，返回圆周率值"""
    pi_estimate = 0.0
    denominator = 1
    sign = 1
    while True:
        term = sign / denominator
        if abs(term) < error:
            break
        pi_estimate += term
        sign *= -1
        denominator += 2
    return pi_estimate * 4

if __name__ == '__main__':
    threshold = float(input())
    result = leibniz_of_pi(threshold)
    print("{:.8f}".format(result))

#兔子繁殖问题
n = int(input())

if n == 1:
    current = 1
    prev = 1
elif n == 2:
    current = 1
    prev = 1
else:
    a, b = 1, 1
    for _ in range(3, n+1):
        current = a + b
        a, b = b, current
    prev = a

ratio = prev / current
print(f"{current} {ratio:.3f}")

#鸡兔同笼
heads, legs = map(int, input().split())
if legs % 2 != 0 or heads <= 0 or legs <= 0:
    print("Data Error!")
else:
    y = (legs - 2 * heads) // 2
    x = heads - y
    if x >= 0 and y >= 0 and (2*x + 4*y) == legs:
        print(f"有{x}只鸡，{y}只兔")
    else:
        print("Data Error!")

#百钱买百鸡A
for x in range(1, 20): 
    for y in range(1, 33):  
        z = 100 - x - y  
        if z % 3 == 0 and 5*x + 3*y + z//3 == 100 and z > 0:
            print(f"{x} {y} {z}")

#求数列前n项的平方和
n = int(input())
sum_squares = n * (n + 1) * (2 * n + 1) // 6
print(sum_squares)

#正负交错数列前N项和
n = int(input())
sum_result = 1.0  
a, b = 1, 2       
sign = -1          
for i in range(2, n+1):
    numerator = i-1
    term = sign * numerator / b
    sum_result += term
    a, b = b, a + b
    sign *= -1
print("{:.6f}".format(sum_result))

#奇数数列求和
n = int(input())
sum_series = n * n
print(sum_series)

#用户登录A
username = input().strip()
password = input().strip()

if username == "admin" and password == "012345":
    print("登录成功")
else:
    print("登录失败")