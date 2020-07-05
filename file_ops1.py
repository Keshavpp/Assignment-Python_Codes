#Chapter 7, file operation, Week 3
fhand = open('text.txt')
count = 0
for line in fhand:
	count = count + 1

print('Line Count:', count)