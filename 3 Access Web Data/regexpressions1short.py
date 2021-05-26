#import regular expression functionality
import re

print(sum([int(n) for n in re.findall('[0-9]+',open('regex_sum_1208519.txt').read())]))
