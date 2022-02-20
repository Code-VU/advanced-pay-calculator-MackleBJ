def calculatePay():
    
    # This first line is provided for you
    try:
        hrs = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
        overtime_hours = 0

        if hrs > 40:
            overtime_hours = hrs - 40
            hrs = hrs - overtime_hours

        pay = (hrs * rate) + (overtime_hours * (rate * 1.5))
        print("Pay: {}".format(pay))

    except:
        print("Error, please enter numeric input")
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()