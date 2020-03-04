#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os					#für Konsolenfunktion
from functions import * 	#Datei.py für wichtige Funktionen


def networkMenue():

	clear()					#Leert die Konsole, aus 'functions'	
	print()					#Leerzeile
	
	#Zeichnen des Interface
	print()
	print("=========================================================")
	print("               Network Configuration")
	print("=========================================================")
	print()
	
	if fileExists("/etc/network/interfaces"):		#wenn die Datei existiert
		f = open("/etc/network/interfaces", "r")	#Datei öffnen
		lines = f.readlines()						#Alle Zeilen einlesen
		
		counter = 1
		for i in range(0, len(lines)):				#Zeilen einzeln durch gehen
			line = lines[i].replace("\n", "")
			if line.find("iface") == 0:				#interface finden
				if line.split(" ")[3] == "static":
					print(counter, ") ", line.split(" ")[1], "(", lines[i + 1].split(" ")[1].replace("\n", ""), ")")
				elif line.split(" ")[3] == "dhcp":
					print(counter , ") ", line.split(" ")[1], " (DHCP)")
				else:
					print(counter , ") ", line.split(" ")[1], " (unknown)")
				counter += 1

	print()
	
	inputVar = input(":")		#Warten auf Eingabe
	
	