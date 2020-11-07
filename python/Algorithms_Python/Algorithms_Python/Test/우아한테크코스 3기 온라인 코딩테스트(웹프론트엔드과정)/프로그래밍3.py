def solution(money, expected, actual):
	betting = 100
	for i in range(len(expected)):
		if money < betting: betting = money; money = 0
		else: money -= betting

		if expected[i] == actual[i]:
			money += betting * 2
			betting = 100
		else:
			betting *= 2

		if money == 0: return 0

	return money

print(solution(1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H'], ['T', 'T', 'H', 'H', 'T', 'T', 'H']))
print(solution(1200, ['T', 'T', 'H', 'H', 'H'], ['H', 'H', 'T', 'H', 'T']))
print(solution(1500, ['H', 'H', 'H', 'T', 'H'], ['T', 'T', 'T', 'H', 'T']))