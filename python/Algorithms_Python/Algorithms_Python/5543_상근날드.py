import sys

# menu = list(map(int, sys.stdin.readlines().split()))
# a = menu[0:3]
# print(a)

menu = [[], []]
for i in range(3):
    menu[0].append(int(input()))
for i in range(2):
    menu[1].append(int(input()))
print(min(menu[0]) + min(menu[1]) - 50)