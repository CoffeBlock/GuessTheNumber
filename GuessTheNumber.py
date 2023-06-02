import random

num = 0
humanguess = 0
digit = 0
maxnum = 1
mininum = 1
wait = 0
guessr = 0


def ttpowermax(repeat):
    repeat = int(repeat)
    if repeat == 0:
        global maxnum
        maxnum = 9
    else:
        while repeat != 0:
            global digit
            maxnum = 10* maxnum
            repeat = repeat - 1

def ttpowermini(repeat):
    repeat = int(repeat)
    if repeat == 0:
        global mininum
        mininum = 0
    else:
        while repeat != 0:
            global digit
            mininum = 10* mininum
            repeat = repeat - 1

def numgen(digit):
    global maxnum
    global num
    ttpowermax(digit)
    maxnum = maxnum - 1
    digit = int(digit)
    ttpowermini(digit - 1)
    num = random.randrange(mininum, maxnum)

def askdigits():
    print("how many digits do you want to guess?")
    wait = 1
    while wait == 1:
        global digit
        userinput = input()
        digit = userinput
        wait = 0

def start():
    wait = 1
    print("welcome to Guess the number!!! [s] to start, [r] for rule")
    while wait == 1:
        userinput = input()
        if userinput == "s":
            wait = 0
        if userinput == "r":
            print ("The rule is: You choose a digit(2 is going to be a number beteewn 10 - 99), tpye a number, see if it is right. All input need to press enter to work.")
        else:
            print ("[s] to start, [r] for rule")
    
def guess(number):
    global guessr
    wait = 1
    print("Guess a number")
    while wait == 1:
        global mininum
        userinput = int(input())
        if userinput < mininum:
            print ("The number is way larger, at least larger than", mininum, ".")
        elif userinput > maxnum:
            print ("The number is way smaller, at least smaller than", maxnum, ".")
        elif userinput < number:
            print ("the number is larger")
            guessr = guessr + 1
        elif userinput > number:
            print ("the number is smaller")
            guessr = guessr + 1
        elif userinput == number:
            print ("you got it in", guessr + 1, "tries")
            exit()






start()
askdigits()
numgen(digit)
guess(num)



