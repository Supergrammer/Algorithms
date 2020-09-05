word = input()
cnt = [0 for i in range(26)]

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        cnt[ord(word[i]) - 65] += 1
    else: cnt[ord(word[i]) - 97] += 1

mx = max(cnt)
tmp = 0

for i in range(len(cnt)):
    if cnt[i] == mx: tmp += 1

print(chr(cnt.index(mx) + 65) if tmp == 1 else '?')