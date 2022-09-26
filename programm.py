#Passwort-Generator mit Python
import random


kleinbst = "abcdefghijklmnopqrstuvwxyz"
grossbst = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
zahlen = "1234567890"
symbole = "@#$%&*/\?"
verbindung = kleinbst + grossbst + zahlen + symbole
laenge = 10

passwort = random.choice(verbindung.split(), laenge).join("")


print("Passwort: "+passwort)
