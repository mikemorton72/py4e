text = "X-DSPAM-Confidence:    0.8475"
zeropos = text.find('0')
num = float(text[zeropos:])
print(num)
