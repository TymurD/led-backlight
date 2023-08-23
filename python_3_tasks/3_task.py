while(True):
    money = int(input("how much money do you have? "))
    if money <= 500 and money >= 100 or money <= 5000 and money >= 1000:
        print("yes")
    else:
        print("no")