def gross_pay_calculator():
    """Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
    Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours."""

    # prompt user for hours and hourly rate as floats 
    hrs = float(input("Enter Hours: ")) 
    hrt = float(input("Enter hourly rate: ")) 

    # conditional if hours are greater than 40, print regular rate PLUS overtime hours * hourly rate * 1.5, else print base rate 
    if hrs > 40.0:
        print(40.0*hrt + (hrs-40.0)*hrt*1.5) 

    # base hourly rate PLUS anything over 40 hours == 1.5*rate  
    else:
        print(hrs*hrt)
