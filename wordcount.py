#get filename and create handle (exit if not found)
fname = input('Enter text file name: ')
try:
    handle = open(fname)
except:
    print("file","'"+fname+"'","not found")
    quit()
worddict = dict()

#create dictionary with count of word occurances
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word = word.lower()
        worddict[word] = worddict.get(word, 0) + 1
#create list of [(v,k) , (v,k), ......]
wordlist = []
for k,v in worddict.items():
    wordlist.append((v,k))
#sort by largest occurance first and print 25 most common
wordlist = sorted(wordlist,reverse=True)
for i in wordlist[:25]:
    print(i[1],i[0])
