from math import*
print("Tere! Olen sinu uus sõber - Python!")
nimi= input("nimi")
print(f"{nimi}")

print(f"{nimi}, oi kui ilus nimi!")
answer = str(input(f"{nimi}! Kas leian Sinu keha indeksi? ja või ei?"))
if answer == "ja":
    pikkus=int(input("pikkus"))
    mass=int(input("mass"))
    d= mass/sqrt(0.01*pikkus)
    if d>=40:
        index="Tervisele ohtlik rasvumine"
    elif 35<=d<=40:
        index="Tugev rasvumine"
    elif 30<=d<=35:
        index="Rasvumine"
    elif 25<=d<=30:
        index="Ülekaal"
    elif 19<=d<=25:
        index="Normaalkaal"
    elif 16<=d<=19:
        index="Alakaal"
    elif 0<=d<=16:
        index="Tervisele ohtlik rasvumine"
    else:
        index="Kahju! See on väga kasulik info!"

    print(f"{nimi}! Sinu keha indeks on:{index}")


else:
    "Kahju! See on väga kasulik info!"



print(f"Kohtumiseni,{nimi}!Igavesti Sinu, Python!")
