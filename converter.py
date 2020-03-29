#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Programm, um Temperaturen umzurechnen
def hauptmenue():
    print("Herzlich Willkommen zum Temperatur-Umrechner!")
    print("Bitte wählen Sie den Umrechnungsmodus:")
    print("(1) Celsius nach Fahrenheit")
    print("(2) Celsius nach Kelvin")
    print("(3) Fahrenheit nach Celsius")
    print("(4) Fahrenheit nach Kelvin")
    print("(5) Kelvin nach Celsius")
    print("(6) Kelvin nach Fahrenheit")
    auswahl = input("Ihre Auswahl: ")
    return auswahl
#Auswahl des Umrechnungsmodus
def moduswahl():
    #Abfrage und Auswahl des Modus
    auswahl = hauptmenue()
    if auswahl == 1:
        #Celsius nach Fahrenheit
        mode = 1
        print("Dieser Modus rechnet Celsius in Fahrenheit um.")
        eingabe = wertabfrage()
        umgerechneteEingabe = celsiusToFahrenheit(mode, eingabe)
        print(eingabe, "Grad Celsius sind ", umgerechneteEingabe, "Grad Fahrenheit.")
        moduswahl()
    elif auswahl == 2:
        #Celsius nach Kelvin
        print("Dieser Modus rechnet Celsius in Kelvin um.")
        eingabe = wertabfrage()
        umgerechneteEingabe = celsiusToKelvin(eingabe)
        print(eingabe, "Grad Celsius sind umgerechnet", umgerechneteEingabe, "Kelvin.")
        moduswahl()
    elif auswahl == 3:
        #Fahrenheit nach Celsius
        mode = 2
        print("Dieser Modus rechnet Fahrenheit in Celsius um.")
        eingabe = wertabfrage()
        umgerechneteEingabe = celsiusToFahrenheit(mode, eingabe)
        print(eingabe, "Grad Fahrenheit sind", umgerechneteEingabe, "Grad Celsius.")
        moduswahl()
    elif auswahl == 4:
        #Fahrenheit nach Kelvin
        mode = 1
        print("Dieser Modus rechnet Fahrenheit in Kelvin um.")
        eingabe = wertabfrage()
        umgerechneteEingabe = fahrenheitToKelvin(mode, eingabe)
        print(eingabe, "Grad Fahrenheit sind", umgerechneteEingabe, "Kelvin.")
        moduswahl()
    elif auswahl == 5:
        #Kelvin nach Celsius
        mode = 2
        print("Dieser Modus rechnet Kelvin in Celsius um.")
        eingabe = wertabfrage()
        umgerechneteEingabe = celsiusToKelvin(mode, eingabe)
        print(eingabe, "Kelvin sind", umgerechneteEingabe, "Grad Celsius.")
        moduswahl()
    elif auswahl == 6:
        #Kelvin nach Fahrenheit
        mode = 2
        print("Dieser Modus rechnet Kelvin in Fahrenheit um.")
        eingabe = wertabfrage()
        umgerechneteEingabe = fahrenheitToKelvin(mode, eingabe)
        print(eingabe, "Kelvin sind", umgerechneteEingabe, "Grad Fahrenheit.")
        moduswahl()
    elif auswahl == "q":
        pass
        exit
    else:
        print("Fehlerhafte Eingabe. Bitte erneut versuchen.")
        moduswahl()

#Definition der Umrechnungsfunktionen
#mode wählt den Berechnungsmodus (hin oder zurück)
def celsiusToFahrenheit(mode, input):
    if mode == 1:
        umgerechneteEingabe = (input * 9/5) + 32
        return umgerechneteEingabe
    elif mode == 2:
        umgerechneteEingabe = (input - 32) * 5/9
        return umgerechneteEingabe
def celsiusToKelvin(mode, input):
    if mode == 1:
        umgerechneteEingabe = (input + 273.15)
        return umgerechneteEingabe
    elif mode == 2:
        umgerechneteEingabe = (input - 273.15)
        return umgerechneteEingabe
def fahrenheitToKelvin(mode, input):
    if mode == 1:
        fToC = celsiusToFahrenheit(2, input)
        umgerechneteEingabe = fToC + 237.15
        return umgerechneteEingabe
    elif mode == 2:
        kToC = celsiusToKelvin(2, input)
        umgerechneteEingabe = (kToC * 9/5) + 32
        return umgerechneteEingabe
def wertabfrage():
    #Fragt den Ausgangswert für die Umrechnung ab und gibt mit eingabe diesen Wert als int zurück
    eingabe = int(input("Bitte geben Sie den zu konvertierenden Wert an: "))
    print("Ihre Eingabe:", eingabe)
    return eingabe

#Einstiegspunkt Programm
moduswahl()
