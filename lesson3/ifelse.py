# Problem 1
from calendar import c


num1 = 2**3
num2 = 3**2
if num1 > num2:
    print(num1)
else:
    print(num2)


# Problem 2
# if a > b and a > c:
    # print(a, "-a больше")
# elif b > a and b > c:
    # print(b)
# else: 
    # print(c)


# Problem 3
a = 17391
b = 546
c = 934

if a % 17 > b % 17 and a % 17 > c % 17:
    print("a больше")
elif b % 17 > a % 17 and b % 17 > c % 17:
    print("b больше")
else:
    print("c больше")


# Problem 4
x = 13

while x < 172:
    x **= 2
print(x)


# Problem 5
num = int(input())

if num % 2 == 0:
    print("DA")
if num % 3 == 0:
    print("Da")
if num ** 2 > 1000:
    print("Da")


# Problem 6

number = int(input())

if number >= 0 and number< 22 or number>=57 and number <101:
    print("Разрашен")
else:
    print("Запрешен")


# Problem 7
if True:
    print("Argen")


# Problem 8
# if age == 18:
#     if height >= 170:
#         if talant == "yes":
#             print("Принят")
