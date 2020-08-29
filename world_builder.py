def word_builder(ltr, pos):
	ltr_new = []
	for num,val in enumerate(ltr):
		# ltr_new.insert(pos[num],val)
		# print(pos[num])
		ltr_new.append(((ltr[pos[num]])))
	return "".join(ltr_new)

	# return ["".join(ltr[pos[num]]) for num in range]

ltr = ["e", "t", "s", "t"]
pos = [3, 0, 2, 1]


print(word_builder(ltr,pos))
# word_builder(ltr,pos)
