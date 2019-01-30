from itertools import permutations

def kmp(s, p):
	"""
	:type s: str
	:type p: str
	:rtype : int
	"""
    next_array = getNext(p)

    i = 0
    j = 0

    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i++
            j++
        else:
            j = next_array[j]

    if j == len(p):
        return i-j
    return -1


def getNext(p):
	"""
	:type p: str
	:rtype : List[int]
	"""
	next_array = []
	next_array.append(-1)
	i = 0
	j = -1

	while i < len(one)-1:
		if j == -1 or one[i] == one[j]:
			i = i + 1
			j = j + 1
			next_array.append(j)
		else:
			j = next_array[j]
			next_array.append(0)
    return next_array


def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """

    all_permutations = list(permutations(range(len(words))))
    combine = set()
    for one in all_permutations:
        temp = ""
        for i in one:
            temp += words[i]
        combine.add(temp)

    result = []
    for one in combine:
		pos = kmp(s, one)
		if result.count(pos) == 0:
			result.append(pos)

	if result.count(-1) > 0:
		result.remove(-1)
    return result
