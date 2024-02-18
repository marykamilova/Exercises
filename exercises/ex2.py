a = int(input())

x1 = a%10
a = a//10
x2 = a%10
a = a//10
x3 = a%10
a = a//10
x4 = a

print(max(x1, x2, x3,x4) - min(x1, x2, x3, x4))