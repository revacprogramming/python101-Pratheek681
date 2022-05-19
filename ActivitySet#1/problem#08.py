# Files

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for i in fh:
    if not i.startswith("X-DSPAM-Confidence:"): 
        continue
    ipos = i.find(':')
    flt = float(i[ipos + 1: ])
    total= total + flt
    count = count + 1

print('Average spam confidence:', total/count)
