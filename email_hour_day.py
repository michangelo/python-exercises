def email_hour_day():
    """
    This program counts the distribution of the hour of the day for each of 
    the messages. You can pull the hour from the "From " line by finding the 
    time string and then splitting that string into parts using the colon 
    character. Once you have accumulated the counts for each hour, print out
    the counts, one per line, sorted by hour as shown below.
    
    python timeofday.py
    Enter a file name: mbox-short.txt
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1
    """
    # first, set conditional to open file and shortcut if file is 'mbox-short.txt'
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)
    # second, set empty dictionary to store hours of day 
    hours_dict = {}
    # pull hour from each day and use .get() idiom
    for line in handle:
        if line.startswith("From "):
            time = line.split()[5]
            hour = time.split(":")[0]
            hours_dict[hour] = hours_dict.get(hour, 0) + 1
            #print(hours_dict)
        tup_lst = list(hours_dict.items()) # create tuple list with .items()
        #print(tup_lst)
    tup_lst.sort()  # sort the list of tuples
    # clean up the print to match exercise by using another for loop
    for l in tup_lst:
        print(l[0], l[1])
    #print(tup_lst)
