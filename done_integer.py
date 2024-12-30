def done_integer():
    """Repeatedly prompts a user for integer numbers
    until user enters "done". Once "done" is entered, 
    print out the largest and smallest of the numbers"""

    largest = None
    smallest = None

    while True:
        num = input("Enter a number: ")
        if num == "done": 
            break
        try: 
            fnum = float(num)
        except:
            print("Invalid input")
            continue
        # print(num)

        # if conditional to set largest and smallest variable from fnum
        if largest is None:
                largest = fnum
        elif fnum > largest:
                largest = fnum
        elif smallest is None:
                smallest = fnum
        elif fnum < smallest:
                smallest = fnum

    # ensure largest and smallest variables are set to type "int"
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))
