#!/usr/bin/python
# Program by Leon Schwarze, 2020
print("Seriennummern-Prüfer - Dieses Programm prüft die Gültigkeit von Seriennummern auf Euro-Scheinen.")
print()
seriennummerEingabe = input("Bitte geben Sie die Seriennummer ein: ")
# Zerlegung der Seriennummer
laendercode = seriennummerEingabe[0]
nutzziffern = seriennummerEingabe[1:10]
pruefziffer = seriennummerEingabe[11]
"""
print(laendercode)
print(nutzziffern)
print(pruefziffer)
"""
# Umrechnung des Ländercodes
liste = ["?", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(27):
    if liste[i] == laendercode:
        laendercodeNummer = str(i)
        # print(laendercodeNummer)
# Zusammensetzung der neuen Nummer
nummerOhnePruef = laendercodeNummer + nutzziffern
# print(nummerOhnePruef)
# Berechnung der Quersumme
quersumme = 0
for zifferBuchstabe in nummerOhnePruef:
    quersumme = quersumme + int(zifferBuchstabe)
# print(quersumme)
pruefDifferenz = quersumme % 9
# print(pruefDifferenz)
if pruefDifferenz == 8:
    pruefVorgabe = 9
elif pruefDifferenz != 8:
    pruefVorgabe = 8 - pruefDifferenz
# print(pruefVorgabe)
if pruefziffer == str(pruefVorgabe):
    print("Die Seriennummer ist gültig.")
elif pruefziffer != str(pruefVorgabe):
    print("Die Prüfziffer ist ungültig und müsste ", pruefVorgabe, "lauten.")
