check_cookies = {"text1" : "not enough",
                 "text2" : "enough",
                 "text3" : "pretty enough",}
while(True):
    try:
        cookies = int(input("how many cookies do you have? "))
        break
    except:
        print("write a number")

if cookies < 100:
    print(check_cookies["text1"])
elif cookies > 500:
    print(check_cookies["text3"])
else:
    print(check_cookies["text2"])