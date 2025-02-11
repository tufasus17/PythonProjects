# testing git

num = int(input())
f = 1
digit = num % 10

while num != 0:
    last_digit = num % 10
    if last_digit < digit:
        f = 0
    else:
        digit = last_digit
    num = num // 10

if f == 0:
    print("NO")
else:
    print("YES")
