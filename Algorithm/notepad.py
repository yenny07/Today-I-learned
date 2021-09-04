count = 0
base = int(input())
num = base
while True:
    share = num // 10
    remainder = num % 10
    middle_num = share + remainder
    new_num = (remainder * 10) + (middle_num % 10)
    count += 1
    if new_num == base:
        break
    num = new_num

print(count)