#Assignment 1- week 1 - Python Data Structures
text = "X-DSPAM-Confidence:    0.8475";
aa = text.find('0')
print(aa)
#a = float(aa)
bb = text.find('5',aa)
cc = text[aa:bb+1]
c = float(cc)
#print(c)