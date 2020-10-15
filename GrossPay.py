hr = input("Enter Hours:")
rt = input('Enter Rate:')
fh = float(hr)
fr = float(rt)
#Input Data
if fh > 40:
    otph = fh-40
    otpp = otph*fr*1.5
    xp = (40*fr) + otpp
#More than 40
else:
    xp = fh*fr
print('Pay:',xp)
