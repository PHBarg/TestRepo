

if_credit = input("what is you credit score? ")

if int(if_credit) >= 600:
    print("Down payment required $" + str(1000000 * .1))
else:
    print("Down payment required $" + str(1000000 * .2))

