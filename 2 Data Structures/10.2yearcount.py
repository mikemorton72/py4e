#open file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#find from line with hour and add running totals to dict
timedict = dict()
for line in handle:
    if not line.startswith('From'): continue
    try:
        time = line.split()[5]
        hour = time.split(':')[0]
        timedict[hour] = timedict.get(hour, 0) + 1
    except: continue

#sort data in increasing order of hour
sortedlist = sorted(timedict.items())
for k,v in sortedlist:
    print(k,v)
