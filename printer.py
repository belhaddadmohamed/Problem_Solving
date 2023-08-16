import math
# The built-in round() function rounds values up and down.
# The math.floor() function rounds down to the next full integer.
# The math.ceil() function rounds up to the next full integer.


# ========================== Functions ================================ 
def printer_1InOne(page):
    print("-> Recto/Verso: " + str(math.ceil(page / 2)))
    print("")
    for x in range(1, page + 1, 2):
        print(str(x), end=",")
    print("")
    for x in range(2, page + 1, 2):
        print(str(x), end=",")


def printer_2InOne(page):
    print("-> Recto/Verso: " + str(math.ceil(page/4)))
    print("")
    for x in range(1,page+1,4):
        print(str(x) + "-" + str(x+1) , end=",")
    print("")
    for x in range(3,page+1,4):
        print(str(x) + "-" + str(x+1) , end=",")


def printer_4InOne(page):
    print("-> Recto/Verso: " + str(math.ceil(page/8)))
    print("")
    for x in range(1,page+1,8):
        print(str(x) + "-" + str(x+3) , end=",")
    print("")
    for x in range(5,page+1,8):
        print(str(x) + "-" + str(x+3) , end=",")


def printer_8InOne(page):
    print("-> Recto/Verso: " + str(math.ceil(page/16)))
    print("")
    for x in range(1,page+1,16):
        print(str(x) + "-" + str(x+7) , end=",")
    print("")
    for x in range(9,page+1,16):
        print(str(x) + "-" + str(x+7) , end=",")



# ========================== Service ================================ 
page = int(input("-> All Pages: "))
x = int(input("-> Copies Per Page: "))

if x == 4:
    printer_4InOne(page)
elif x == 8:
    printer_8InOne(page)
elif x == 2:
    printer_2InOne(page)
elif x == 1:
    printer_1InOne(page)

print("")
print("")
input("press any key to close")

