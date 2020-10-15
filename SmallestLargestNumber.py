largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        numb = float(num)
    except:
        print("Invalid input")
        continue
    for value in [numb] :
        if largest is None:
            largest=value
        elif value > largest:
            largest=value
        if smallest is None:
            smallest=value
        elif value < smallest:
            smallest=value
small=int(smallest)
large=int(largest)
print("Maximum is", large)
print("Minimum is", small)
