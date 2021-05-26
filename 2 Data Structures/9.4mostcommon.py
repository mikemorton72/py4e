# receive file
fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)

#create dictionary for each email addr and total occurances
ddd= dict()
for line in handle:
    if line.startswith('From:'):
        words = line.split()
        ddd[words[1]]= ddd.get(words[1],0) + 1

#find most common email addr
bigname = None
bigcount = None
for k,v in ddd.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigname = k
print(bigname, bigcount)
