principal = True
rate = True
time = True

while principal:
    principal = float(input("Enter the principal amount: "))

    if principal < 0:
        print("Principal can't be equal to zero!")
    else:
        break
while rate:
    rate = float(input("Enter the interest rate: "))

    if rate < 0:
        print("Interest Rate can't be equal to zero!")
    else:
        break
while time:
    time = int(input("Enter time in years: "))

    if time < 0:
        print("Time can't be equal to zero!")
    else:
        break
total = principal * pow((1 + rate/100), time)


print(f"Your principal amount is Php {principal}.")
print(f"Your rate is {rate}.")
print(f"The number of year(s) is {time}.")
print(f"The balance after {time} year(s) is Php {total:.2f}.")