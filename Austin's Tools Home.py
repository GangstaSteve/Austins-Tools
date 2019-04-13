from colorama import Fore, Back, Style
import colorama
colorama.init()
start = input("Do you want to start Austin's Tool's? Y/n> ")
startboolanimateint = 0
startbool = False
if start == "y" or "Y" or "Yes" or "yes" or "ya" or "YA" or "Ya" or "yeah" or "Yeah" or "YEAH" or "YES" or "oh yeah yeah" or "OH YEAH YEAH":
    startbool = True
    def WholeThing2():
        import time
        import random
        import os
        import pip
        import re
        redc = Fore.RED
        cyanc = Fore.CYAN
        blackc = Fore.BLACK
        bluec = Fore.BLUE
        lightredc = Fore.LIGHTRED_EX
        resetc = Fore.RESET
        background = Back.WHITE
        whitec = Fore.WHITE
        print(
            cyanc+"____________________________________________________________________________________________________________")
        time.sleep(.3)
        print(
            redc+"       d8888                   888    d8b         d8b              88888888888                888           ")
        time.sleep(.3)
        print(
                 "      d88888                   888    Y8P         88P                  888                    888          ")
        time.sleep(.3)
        print(
                 "     d88P888                   888                8P                   888                    888          ")
        time.sleep(.3)
        print(
                 "    d88P 888 888  888 .d8888b  888888 888 88888b. \"  .d8888b           888   .d88b.   .d88b.  888 .d8888b  ")
        time.sleep(.3)
        print(
                 "   d88P  888 888  888 88K      888    888 888 \"88b   88K               888  d88\"\"88b d88\"\"88b 888 88K      ")
        time.sleep(.3)
        print(
                 "  d88P   888 888  888 \"Y8888b. 888    888 888  888   \"Y8888b.          888  888  888 888  888 888 \"Y8888b. ")
        time.sleep(.3)
        print(
                 " d8888888888 Y88b 888      X88 Y88b.  888 888  888        X88          888  Y88..88P Y88..88P 888      X88 ")
        time.sleep(.3)
        print(
                 "d88P     888  \"Y88888  88888P'  \"Y888 888 888  888    88888P'          888   \"Y88P\"   \"Y88P\"  888  88888P'")
        time.sleep(.3)
        print(
            cyanc+"______________________________________________________________________________________________________________")
        print("")
        print("")
        print("")
        print(resetc+"1."+redc+"Text Games List     "+resetc+"11.")
        time.sleep(.3)
        print("2."+redc+"Great Calculators   "+resetc+"12.")
        time.sleep(.3)
        print("3."+redc+"Machine Learning    "+resetc+"13.")
        time.sleep(.3)
        print("4."+redc+"Hacking             "+resetc+"14.")
        time.sleep(.1)
        print("5."+redc+"Macros and bots     "+resetc+"15.")
        time.sleep(.3)
        print("6."+redc+"UNKNOWN             "+resetc+"16.")
        time.sleep(.3)
        print("7."+redc+"UNKNOWN             "+resetc+"17.")
        time.sleep(.3)
        print("8.                    18.")
        time.sleep(.3)
        print("9.                    19.")
        time.sleep(.3)
        print("10.                   20.")
        print("")
        print("\033[0m")
        time.sleep(.5)
        Input1 = input("Select a number from the list: ")
        if Input1 == "1":
            print("")
            print(cyanc+"_________                              ")
            print("__  ____/_____ _______ ________________")
            print("_  / __ _  __ `/_  __ `__ \  _ \_  ___/")
            print("/ /_/ / / /_/ /_  / / / / /  __/(__  ) ")
            print("\____/  \__,_/ /_/ /_/ /_/\___//____/  " + whitec)
            print("_______________________________________" + resetc)
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("1."+redc+"Guess the number" + resetc)
            print("2."+redc+"Tic Tac Toe"+ resetc)
            print("3.  ")
            print("4.  ")
            print("5.  ")
            print("6.  ")
            print("7.  ")
            print("8.  ")
            print("9.  ")
            print("0."+"Return to menu ")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            Input1_1 = input("Select a number from the list: ")
            if Input1_1 == "1":
                limit = 100
                randomnum = random.randint(1, 100)
                guessgame = True
                guesscount = 0
                print("\n\n\n\n\n\n\n\nthis is a simple guessing game. Win to return to menu\n\n\n\n")
                while guessgame:
                    try:
                        guess = input("guess a number between 1 to 100: ")
                        if int(guess) > randomnum and int(guess) <= 100:
                            guesscount += 1
                            if guesscount == 1:
                                print("Guess lower! You have guessed Once\n")
                            else:
                                print("Guess lower! You have guessed " + str(guesscount) + " times\n")

                        elif int(guess) < randomnum and int(guess) <= 100:
                            guesscount += 1
                            if guesscount == 1:
                                print("Guess higher! You have guessed Once\n")
                            else:
                                print("Guess higher! You have guessed " + str(guesscount) + " times\n")
                        elif int(guess) > 100:
                            guesscount += 2
                            print(
                                "Im adding two points for your stupidity. I LITERALLY SAID GUESS A NUMBER BETWEEN 1 AND 100. " + "You have guessed " + str(
                                    guesscount) + " times\n")
                        elif int(guess) == randomnum:
                            print("You WIN! returning to the menu in 5 seconds.")
                            time.sleep(1)
                            print("1.")
                            time.sleep(1)
                            print("2..")
                            time.sleep(1)
                            print("3...")
                            time.sleep(1)
                            print("4.")
                            time.sleep(1)
                            print("5..")
                            guessgame = False
                            startbool = False
                            startbool = True

                    except ValueError:
                        ValueErrorinput = input("Invalid character. Would you like to exit this game?(y/n): ")
                        time.sleep(1)
                        guessgame = False
                        guessgame = True
            elif Input1_1 == "0":
                startbool = False
                time.sleep(1)
                print("\n\n\n")
                print("RESTARTING")
                startbool = True
            elif Input1_1 == "2":
                import time
                import random

                O = "OOO"
                X = "XXX"
                a = "1  "
                b = "2  "
                c = "3  "
                d = "4  "
                e = "5  "
                f = "6  "
                g = "7  "
                h = "8  "
                i = "9  "
                Onum = ""
                Xnum = ""
                runTTT = True
                print(a + "|" + b + "|" + c)
                print("___|___|___")
                print(d + "|" + e + "|" + f)
                print("___|___|___")
                print(g + "|" + h + "|" + i)
                print("   |   |   ")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                wonTTT = False
                while runTTT:
                    if a and b and c and d and e and f and g and h and i in [O, X] and not wonTTT:
                        print("Board filled! you got a tie.")
                        runTTT = False
                        startbool = False
                        time.sleep(1)
                    Xnum = input("Player1(X) choose a number: ")
                    if Xnum == "1" and a != O and a != X:
                        a = X
                    elif Xnum == "2" and b != O and b != X:
                        b = X
                    elif Xnum == "3" and c != O and c != X:
                        c = X
                    elif Xnum == "4" and d != O and d != X:
                        d = X
                    elif Xnum == "5" and e != O and e != X:
                        e = X
                    elif Xnum == "6" and f != O and f != X:
                        f = X
                    elif Xnum == "7" and g != O and g != X:
                        g = X
                    elif Xnum == "8" and h != O and h != X:
                        h = X
                    elif Xnum == "9" and i != O and i != X:
                        i = X
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print(a + "|" + b + "|" + c)
                    print("___|___|___")
                    print(d + "|" + e + "|" + f)
                    print("___|___|___")
                    print(g + "|" + h + "|" + i)
                    print("   |   |   ")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    if a == X and e == X and i == X:
                        print("X wins!")
                        wonTTT = True
                        break
                    elif a == X and b == X and c == X:
                        print("X wins!")
                        wonTTT = True
                        break
                    elif a == X and d == X and g == X:
                        print("X wins!")
                    if a and b and c and d and e and f and g and h and i in [O, X] and not wonTTT:
                        print("Board filled! you got a tie.")
                        runTTT = False
                        startbool = False
                        time.sleep(1)

                    Onum = input("Player2(O)choose a number(1-9): ")

                    if Onum == "1" and a != O and a != X:
                        a = O
                    elif Onum == "2" and b != O and b != X:
                        b = O
                    elif Onum == "3" and c != O and c != X:
                        c = O
                    elif Onum == "4" and d != O and d != X:
                        d = O
                    elif Onum == "5" and e != O and e != X:
                        e = O
                    elif Onum == "6" and f != O and f != X:
                        f = O
                    elif Onum == "7" and g != O and g != X:
                        g = O
                    elif Onum == "8" and h != O and h != X:
                        h = O
                    elif Onum == "9" and i != O and i != X:
                        i = O
                    print(a + "|" + b + "|" + c)
                    print("___|___|___")
                    print(d + "|" + e + "|" + f)
                    print("___|___|___")
                    print(g + "|" + h + "|" + i)
                    print("   |   |   ")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    if a == O and e == O and i == O:
                        print("O wins!")
                        wonTTT = True
                        break
                    if a and b and c and d and e and f and g and h and i in [O, X] and not wonTTT:
                        print("Board filled! you got a tie.")
                        runTTT = False
                        startbool = False
                        time.sleep(1)


    WholeThing2()
    def WholeThing1():
        print("temporary")

elif start == "n" or "N" or "No" or "NO" or "no" or "Nah" or "nah" or "na" or "Na":
    print("Ok. The process will terminate.")
    startbool = False
else:
    print("I will take that as a yes.")
    import time
    time.sleep(3)
while startbool:
    WholeThing2()






