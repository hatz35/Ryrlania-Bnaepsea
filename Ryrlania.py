import random

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
    minchar = int(input("\n\nEnter Minimum Individuals to be in the chapter"))
    maxchar = int(input("Enter Maximum Individuals to be in the chapter"))
    mintop = int(input("Enter Minimum Topics to be in the chapter"))
    maxtop = int(input("Enter Maximum Topics to be in the chapter"))

    k = input("Enter Chapter Number")
    print(f"---- Chapter {k} ---- \nMain: {select(Char, minchar, maxchar)} \nSettgs/Topic: {select(Top, mintop, maxtop)}")

def menu():
    mainloop(gettopics(), getchar())

#GLOBAL
menu()
