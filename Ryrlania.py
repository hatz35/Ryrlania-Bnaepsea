import random

while True:
    ryrlans = []
    places = []

    minryr = int(input("Enter Minimum Ryrlans to be in a group"))
    maxryr = int(input("Enter Maximum Ryrlans to be in a group"))
    ryrselected = random.randrange(minryr, maxryr + 1)
    for i in range(ryrselected):
        ryrlans.append(random.randrange(1, 22))

    L = ["Donyard", "Ankchers", "Luu", "Radiance", "Chyre-Chavant", "Explorer-Wanderer", "Mice", "Reiri-Sam's House", "Sod-1-Rosarhis", "BOC-Amsek-Psuupe", "Reha", "Kakuka&Drago Guild", "Omri-Rhys Guild", "Echelon", "Horizon", "Onger", "Xiderenj", "Warg", "Auray", "Ophale", "Qaqzae", "Jilm", "Ahero", "Blu", "Ahero", "Exiger Base", "Rafz", "Shiverd-Norka","Fervo", "Fiola", "Central Fye", "Interlaum", "Mentou", "Sydys-Entroka", "OdysseyGuild", "Ryrlan", "Central Skoo"]

    ll = int(input("Enter Number of Topics could be in the chapter"))
    for j in range(ll):
        places.append(random.choice(L))

    k = input("Enter Chapter Number")
    print(f"Princess: Chapter {k}!! Roll No.! " + str(ryrlans) + " Gooooo " + str(places))
