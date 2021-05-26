import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#lst = [v,k for k,v in counts.items()]
lst = sorted([(v,k) for k,v in counts.items()],reverse=True)
for i in lst:
    print(i[0],i[1])
