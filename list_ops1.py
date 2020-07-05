##Chapter 8, Lists, Week 4, Assignment1
#Use the file name romeo.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print('File cannot be opened:',fname)
	quit()
ans =list()
for lines in fh:
	names = lines.rstrip().split()
	for item in names:
		if item in ans:
			continue
		else:
			ans.append(item)

ans.sort()
print(ans)