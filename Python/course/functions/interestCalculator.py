#-------interset Caculation Function-------#
def interestCalculator(principal,rate,time):
    si = (principal * rate * time) / 100
    return si
def simpleInterest():
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest: "))
    time = float(input("Enter Time in years: "))
    si = interestCalculator(principal,rate,time)
    print(f"Simple Interest is: {si}")
    
simpleInterest()
