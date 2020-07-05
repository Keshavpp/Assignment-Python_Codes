###Chapter 10, Tupples, Week 6, Assignment
#Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print('File cannot be opened:',fname)
	quit()
hours = dict()

arr = list()
for line in fh:
	if not line.startswith("From ") : continue
	spl = line.rstrip().split()
	main = spl[5]
	hour = main.split(':')
	hh = hour[0]
	arr.append(hh)

for i in arr:
	hours[i] = hours.get(i,0) +1

hss = list()

for key,value in hours.items():
	hss.append((key,value))

hss.sort()

for k,v in hss:
	print(k,v)	