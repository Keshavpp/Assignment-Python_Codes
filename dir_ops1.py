###Chapter 9, Doctionaries, Week 5, Assignment
#Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print('File cannot be opened:',fname)
	quit()
count = 0
names = dict()
tell = list()
for line in fh:
    if not line.startswith("From ") : continue
    annns = line.rstrip().split()
    mains = annns[1]
    tell.append(mains)
    #print(ans[0])

for tel in tell:
	names[tel] = names.get(tel, 0) + 1

l1 = names.keys()
l2 = names.values()
mm = max(l2)
for key,value in names.items():
	if value == mm:
		print(key,names[key])
#print(tell)