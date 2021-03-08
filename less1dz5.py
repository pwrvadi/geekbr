viruchka = int(input("skolko vi zarabotali"))
ubitok = int(input("skolko vi potratili"))
if viruchka > ubitok:
    print("pozdravlyaem, vi v pluse")
    worker = int(input("skolko ludey rabotaet?"))
else:
    print("shto-to vi delaete ne tak. Vi v minuse, gospodin biznesmen")
    quit()

renta = viruchka - ubitok
sotrudnik = renta  / worker
print("kompaniya zarabotala", renta, "odin sotrudnik prinosit vam", sotrudnik)
