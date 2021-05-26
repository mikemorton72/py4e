#Hour and Rate Calculator
def computepay(h,r):
    if hrs <=40:
        pay = hrs *payrate
    elif hrs >40:
        pay = 40*payrate + (hrs-40)*payrate*1.5
    return pay
hrs = float(input("Enter Hours: "))
payrate = float(input("Enter Rate: "))
print('Pay '+str(computepay(hrs,payrate)))
