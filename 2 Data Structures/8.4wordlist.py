
#Use with Romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    linewords = line.split()
    for word in linewords:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)
