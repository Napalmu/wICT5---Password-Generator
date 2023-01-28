#Salasana generaattori JM
from random import choice
from random import randint
import time

def luoSalasana(pituus):
    x = 0
    salasana = ""
    while x <= int(pituus)-1:
        salasana += choice(pohja)
        x += 1
    return salasana

def addJono(oma):
    x = 0
    salasana = ""
    while x <= int(pituus)-1-len(oma):
        salasana += choice(pohja)
        x += 1
    N = randint(0, len(annettu))
    salasana = salasana[:N] + str(oma) + salasana[N:]#Annettu merkkijono satunnaiseen paikkaan salasanaa.
    return salasana

def tarkistaPituus():
    pituus = None
    while pituus is None:
        pituus = input("Kuinka pitkän salasanan haluat? >")
        try:
            pituus = int(pituus)
            if pituus > 0:#Tarkistetaan, onko numero positiivinen.
                continue
            else:
                print("\nVirheellinen syöte, syötä positiivinen numero!")
                pituus = None
        except ValueError:
            print("\nVirheellinen syöte, syötä numero\n")
            pituus = None
       
    return pituus

#Muuttuja, josta choice metodi poimii halutun määrän merkkejä satunnaisessa järjestyksessä.
pohja = "123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

print("SALASANA GENERAATTORI\n")
print("Yleistä: ")
print("Salasanan tulisi olla vähintään 12 merkkiä.")
print("Se ei saisi olla pelkästään yksittäisiä sanoja, koska ne on helppo murtaa.")
print("Tämä ohjelma luo salasanan, joka sisältää numeroita ja kirjaimia.\nHalutessaan salasanaan voi sisällyttää jonkin merkkiyhdistelmän.\n")


#Silmukka, jonka avulla käyttäjä voi suorittaa lopussa ohjelman uudelleen.
jatkuu = 0
while jatkuu == 0:
        #Pyydetään käyttäjältä syöte aliohjelmaan, joka varmistaa, että annettu arvo on numero.
        pituus = tarkistaPituus()
        oma = input("\nHaluatko sisällyttää salasanaan jonkun sanan/jonon?\nHuom. Jos sisällytät erikoismerkkejä, ei ole taattua, että salasana toimii kaikkialla.(joo/ei) >")
        
        if oma == "joo":
            annettu = input("Anna merkit: >")
            #Tarkistetaan annetun merkkijonon pituus, se ei voi ylittää haluttua salasanan pituutta.
            if int(len(annettu)) <= int(pituus):
                time.sleep(0.5) #Sleep -metodilla tyyliä ohjelmaan.
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                print("Luotu uniikki salasanasi annetulla lisäyksellä: ",addJono(annettu))#Tulostetaan aliohjelman luoma merkkijonolla höystetty salasana.
            else:
                print("Annettu sana/jono ei voi olla pidempi kuin annettu pituus.")

        
        else:
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            print("Luotu uniikki salasanasi: ",luoSalasana(pituus))#Tulostetaan salasana, jos merkkijonoa ei haluta lisätä.
        print()
        time.sleep(1)
        jatkuuko = input("Haluatko luoda uuden salasanan? (joo/ei) >")#Annetaan mahdollisuus luoda uusi salasana.
        if jatkuuko == "joo":
            continue
        else:
            jatkuu = 1

input()
