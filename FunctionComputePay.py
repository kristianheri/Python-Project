def computepay(hours, rate) :
    if hours > 40:
        oth = hours-40
        otp = oth*rate*1.5
        pay = (40*rate) + otp
    #More than 40
    else:
        pay = hours*rate
    return pay

hr = input("Enter Hours:")
rt = input('Enter Rate:')
fh = float(hr)
fr = float(rt)

xp = computepay(fh,fr)

print('Pay',xp)
