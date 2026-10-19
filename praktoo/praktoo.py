import math

# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.

# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:

# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

# ESIMENE ÜLESANNE

# print("Tere, maailm!")
# nimi = input("Mis on sinu nimi?")
# print("Tere, maailm! Tervitan sind", nimi)
# N = input("Kui vana sa oled?")
# print("Tere, maailm! Tervitan sind", nimi, "! Sa oled", N, "aastat vana.")

# TEINE ÜLESANNE

# a) vanus = 18 V: <class: 'int'>
# b) eesnimi = "Jaak" V: <class: 'str'>
# c) pikkus = 16.5 V: <class: 'float'>
# d) kas_käib_koolis = True v: <class: 'bool'>
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida? V: False ja kasutamas if funktsiooni, ma arvan
# Kirjuta kood tüüpide kontrollimiseks.


# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_kaib_koolis = True

# print(eesnimi, "on", vanus, "aastat vana ja", pikkus, "pikk.")

# if kas_kaib_koolis == True:
#     print(eesnimi, "kaib koolis.")
# else:
#     print(eesnimi, "ei kai koolis.")

# print(type(vanus))
# print(type(eesnimi))
# print(type(pikkus))
# print(type(kas_kaib_koolis))

# KOLMAS ÜLESANNE

# from random import *
# kommide_arv=randint(1, 100)
# print("laual on", kommide_arv, "kommi.")
# mitu_ara_vota=int(input("mitu kommi tahad ära võta? =>"))
# kommide_arv -= mitu_ara_vota
# print("laual on nüüd", kommide_arv, "kommi.")

# NELJAS ÜLESANNE

# u = float(input("mis oli puu ümbermõõt")) # märkasin, et int läheb esimesena.... 
# lm = u/math.pi
# print("puu läbimõõt on", int(lm))

VIIES ÜLESANNE

a=int(input("sisesta esimene külg"))
b=int(input("sisesta teine külg"))
d = a + b
print("ristküliku diagonaal on",d,"m pikk.")

VIIES ÜLESANNE

a=int(input("sisesta esimene külg"))
b=int(input("sisesta teine külg"))
d = a + b
print("ristküliku diagonaal on",d,"m pikk.")

# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.

# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:

# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

# ESIMENE ÜLESANNE

# print("Tere, maailm!")
# nimi = input("Mis on sinu nimi?")
# print("Tere, maailm! Tervitan sind", nimi)
# N = input("Kui vana sa oled?")
# print("Tere, maailm! Tervitan sind", nimi, "! Sa oled", N, "aastat vana.")

# TEINE ÜLESANNE

# a) vanus = 18 V: <class: 'int'>
# b) eesnimi = "Jaak" V: <class: 'str'>
# c) pikkus = 16.5 V: <class: 'float'>
# d) kas_käib_koolis = True v: <class: 'bool'>
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida? V: False ja kasutamas if funktsiooni, ma arvan
# Kirjuta kood tüüpide kontrollimiseks.


# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_kaib_koolis = True

# print(eesnimi, "on", vanus, "aastat vana ja", pikkus, "pikk.")

# if kas_kaib_koolis == True:
#     print(eesnimi, "kaib koolis.")
# else:
#     print(eesnimi, "ei kai koolis.")

# print(type(vanus))
# print(type(eesnimi))
# print(type(pikkus))
# print(type(kas_kaib_koolis))

# KOLMAS ÜLESANNE

from random import *
# kommide_arv=randint(1, 100)
# print("laual on", kommide_arv, "kommi.")
# mitu_ara_vota=int(input("mitu kommi tahad ära võta? =>"))
# kommide_arv -= mitu_ara_vota
# print("laual on nüüd", kommide_arv, "kommi.")

# NELJAS ÜLESANNE

# u = float(input("mis oli puu ümbermõõt")) # märkasin, et int läheb esimesena.... 
# lm = u/math.pi
# print("puu läbimõõt on", int(lm))

# VIIES ÜLESANNE

# a=int(input("sisesta esimene külg"))
# b=int(input("sisesta teine külg"))
# d = a + b
# print("ristküliku diagonaal on",d,"m pikk.")

# Kuues ülesanne

# Leidke järgnevast näiteprogrammist loogiline viga:
# aeg = int(input("Mitu tundi kulus sõiduks? ")) 
# teepikkus = int(input("Mitu kilomeetrit sõitsid? ")) #peab kasutama int, mitte float kui numbrid on reaalarvud
# kiirus = round(teepikkus/aeg,2) # valem on vale 

# print("Sinu kiirus oli ",str(kiirus)," km/h") # Peab kasutama komasid mitte pluss märgid. 

# seitsmes ülesanne



# kaheksandas ülesanne

# print("   @..@")
# print("  (----)")
# print(" ( \__/ )")
# print("  ^^ "" ^^")

# uheksandas ulesanne

# a = int(input("vali arv esimese küljele"))
# b = int(input("vali arv teise küljele"))
# c = int(input("vali arv kolmas küljele"))
# abc = a + b + c

# print("su kolmnurk ümbermõõt on", abc, "cm")

# viimane ülesanne