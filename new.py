arr = []
def arrProcessor(arr):
	high_odd = 0
	for i in arr:
		if i%2!=0:
			if i>high_odd:
				high_odd = i
	print(high_odd)
while 1:
    s1 = int(input())
    if s1<0:
        break
    arr.append(s1)
arrProcessor(arr)