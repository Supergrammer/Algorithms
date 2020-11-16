def solution(participant, completion):
	retired = {}
	
	for part in participant:
		if retired.get(part):
			retired[part] += 1
		else:
			retired[part] = 1

	for comp in completion:
		retired[comp] -= 1

	for name in retired.keys():
		if retired[name]:
			return name

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))