def solution(gems):
	answer = [1, len(gems)]
	branch = {}

	for gem in gems:
		if branch.get(gem):
			continue
		else:
			branch[gem] = 0

	gem = len(branch)
	count = 1
	left, right = 0, 0
	branch[gems[0]] = 1

	while left != len(gems) and right != len(gems):
		if count == gem and answer[1] - answer[0] > right - left:
			answer = [left + 1, right + 1]
		
		if count < gem:
			right += 1
			if right >= len(gems):
				break
			if branch[gems[right]] == 0:
				count += 1
			branch[gems[right]] += 1
		else:
			branch[gems[left]] -= 1
			if branch[gems[left]] == 0:
				count -= 1
			left += 1

	return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))