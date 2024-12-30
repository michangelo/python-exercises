def letter_grade():
    "Program to prompt for a score between 0.0 and 1.0."

    """>= 0.9     A
       >= 0.8     B
       >= 0.7     C
       >= 0.6     D
       < 0.6      F"""

    # prompt to enter score 
    score = input("Enter Score: ")

    # if score != float, print error and exit
    try:
        score = float(score)
    except:
        print("Bad score. Try again! Hint: Use a float")
        exit()

    # if the score is out of range, print an error and exit
    if score < 0.0 or score > 1.0:
        print("Error: out of range")
        exit()
        
    # if score is in range, assign grade letter  
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
