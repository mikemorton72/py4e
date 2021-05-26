#import regular expression functionality
import re

#create handle, blank number list, and sum variable
numlst = list()
handle = open('regex_sum_1208519.txt')
sum = 0

#iterate through each line and add numbers to numlst
for line in handle:
    nums = re.findall('[0-9]+',line)
    if nums != []:
        for i in nums:
            numlst.append(i)
for num in numlst:
    sum = sum + int(num)

print(sum)
