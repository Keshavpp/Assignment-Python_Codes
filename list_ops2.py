##Chapter 8, Lists, Week 4, Assignment2
#Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print('File cannot be opened:',fname)
	quit()
count = 0
for line in fh:
    if not line.startswith("From ") : continue
    ans = line.rstrip().split()
    print(ans[1])
    count = count +1
print('There were',count,'lines in the file with From as the first word')    