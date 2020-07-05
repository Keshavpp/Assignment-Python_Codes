#Chapter 7, file operation, Week 3, Assignment2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print('File cannot be opened:',fname)
	quit()
summ =0
l =0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    itt = line[20:26]
    i = float(itt)
    summ = summ + i
    l = l + 1
aa = summ/l
ans = round(aa,15)
print("Average spam confidence:",ans)
