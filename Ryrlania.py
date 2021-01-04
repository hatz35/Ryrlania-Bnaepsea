import random

num = int(input("How many times you wanna do?"))
isFast = False

def clear_screen():
    print("\033[H\033[J")

while True:
    kk = input("Wanna do Fast?\n Press 1 for Yes\n Press 2 for No\n")

    if kk == "1":
        isFast = True
        break
    elif kk == "2":
        isFast = False
        break
    else:
        print("Try Again")

k = input("Enter Chapter Number")

clear_screen()
def getword(n):
    #put text file in the same directory
    nameoftextfile = "Words.txt"
    texto = open(nameoftextfile, "r")
    a = texto.readlines()
    #print(a) #test
    for i in range(n):
        print(random.choice(a))

def gettopics():
    #put text file in the same directory
    nameoftextfile = "Topics.txt"
    texto = open(nameoftextfile, "r")
    a = texto.read()
    print(a) #test
    return[i.strip() for i in a.split(",")]

def getchar():
    #put text file in the same directory
    nameoftextfile = "Characters.txt"
    texto = open(nameoftextfile, "r")
    a = texto.read()
    print(a) #test
    return [i.strip() for i in a.split(",")]


def select(mainlist, min, max):
    try:
        toselect = random.randint(min, max)
        outlist = random.sample(mainlist, toselect)
        return str(outlist)
    except ValueError as r:
        print(r, "\nError 01\n\n\n\n")
        menu()

def mainloop(Top, Char):
    for i in range(num):
        if isFast == False:
            minchar = int(input("\n\nEnter Minimum Individuals to be in the chapter"))
            maxchar = int(input("Enter Maximum Individuals to be in the chapter"))
            mintop = int(input("Enter Minimum Topics to be in the chapter"))
            maxtop = int(input("Enter Maximum Topics to be in the chapter"))

            print(f"---- Chapter {k} ---- \nMain: {select(Char, minchar, maxchar)} \nSettgs/Topic: {select(Top, mintop, maxtop)}\n")
            #print("\n")
            #getword(random.randint(1, 10))
        else:
            minchar = random.randrange(1, 5)
            maxchar = random.randrange(minchar+1, 10)
            mintop = random.randrange(1,6)
            maxtop = random.randrange(mintop+1,10)
            print(f"---- Chapter {k} ---- \nMain: {select(Char, minchar, maxchar)} \nSettgs/Topic: {select(Top, mintop, maxtop)}\n")


def menu():
    mainloop(gettopics(), getchar())

#GLOBAL
menu()
