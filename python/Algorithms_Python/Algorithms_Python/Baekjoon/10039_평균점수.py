score = []

for i in range(5):
    inp = int(input())
    if inp < 40: inp = 40
    score.append(inp)

print(int(sum(score) / len(score)))