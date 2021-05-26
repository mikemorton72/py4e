#creat min and max variables
biggest = None
smallest = None
#start while loop
while True:
    n = input('> ')
    #exit loop if user enters 'done'
    if n == 'done':
        break
    #check if input is valid, outputs error and returns to top of loop if invalid
    try:
         n = float(n)
    except:
        print('Invalid input')
        continue
    #see if iteration is biggest and save if so
    if biggest is None:
        biggest = n
    elif biggest < n:
        biggest = n
    #see if iteration is smallest and save if so
    if smallest is None:
        smallest = n
    elif smallest > n:
        smallest = n
print('Maximum is',str(biggest))
print('Minimum is',str(smallest))
