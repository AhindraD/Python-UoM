largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        currNum= int(num)
    except:
        print('Invalid input')


    if largest is None:
        largest= currNum
    elif largest<currNum:
        largest= currNum

    if smallest is None:
        smallest= currNum
    elif smallest>currNum:
        smallest= currNum


print("Maximum is", largest)
print("Minimum is", smallest)