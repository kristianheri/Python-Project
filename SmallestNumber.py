smallest_so_far=None
print('Before')
for value in [9,41,12,3,74,15] :
    if smallest_so_far is None:
        smallest_so_far=value
    elif value < smallest_so_far:
        smallest_so_far=value
    print(smallest_so_far, value)
print ('Afer', smallest_so_far)
