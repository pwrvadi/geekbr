age = (int(input("vvedite vash vozrast >   ")))
if age >= 18:
    print("Spasibo, vozrast prinyat")
else:
    print("Eta programma sozdana dlya ludey vozrastom 18+")
    quit()
weight = (int(input("vvedite vash ves >  ")))
growth = (int(input("vvedite vash rost > ")))
if growth - weight <= 100:
    print("kushayte pomenshe")
else:
    print("kushayte pobolshe")
