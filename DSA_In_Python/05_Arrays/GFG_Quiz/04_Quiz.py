check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'

for c in (check1,check2,check3):
	print(c)

testList = [1,2]

print(testList * 2)