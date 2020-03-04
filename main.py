#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os						#für Systemfunktionen
import sys						#für Konsolenfunktion (z.B. exit)
import socket					#für Systeminformationen
from config	import * 			#Datei.py für das Config-Menue
from functions import * 		#Datei.py für wichtige Funktionen
from network import *			#Datei.py für Netzwerkkonfigurationen
from serverfunction import *	#Datei.py für Serverfunktionen

#Globale Variablen definieren
computerName = ""
domainName = ""
remoteStatus = ""

#Python Versionscheck
if not sys.version.split(".")[0] == "3":						#String teilen und vor dem ersten Punkt nach 3 Suchen
		print("Bitte Python Version 3 oder höher verwenden!")	#Fehlermeldung
		exit()													#Script beenden

def getSysInfos():
	print("Inspecting System...")
	
	#Um die globalen Variablen in dieser Funktion zu verwenden
	global computerName, domainName, remoteStatus
	
	
	computerName = socket.gethostname()		#Computernamen auslesem
	domainName = socket.getfqdn()			#Domainnamen auslesen

	#Checken ob SSH installiert ist
	if os.path.isfile('/etc/init.d/ssh'):
		remoteStatus = "ssh"
	#elif:
		#hier falls andere Remoteeinstellungen aktiv sind
	else:
		remoteStatus = "disabled"


#Funktion Hauptmenü
def menue():

	clear()					#Leert die Konsole, aus 'functions'	
	print()					#Leerzeile
	
	getSysInfos() 			#Abrufen der Systeminformationen
	
	#Zeichnen des Interface
	print()
	print("=========================================================")
	print("               Server Configuration")
	print("=========================================================")
	print()
	
	print(" 0) Zurück zum Terminal")
	print()
	
	print(" 1) Domain/Workgroup:			 	 Domain: ", domainName)
	print(" 2) Computername:		        	", computerName)
	print(" 3) Lokalen Benutzer hinzufügen")
	print(" 4) Remote Management konfigurieren		", remoteStatus)
	print()
	
	print(" 5) Update Einstellungen")
	print(" 6) Download und Installation von Updates")
	print()
	
	print(" 7) Netzwerkeinstellungen")
	print(" 8) Datum und Uhrzeit")
	print(" 9) Zusatzsoftware installieren und konfigurieren")
	print()
	
	print("10) Benutzer abmelden")
	print("11) Server Neu starten")
	print("12) Server Herunterfahren")

	print()
	
	
	inputVar = input(":")		#Warten auf Eingabe
	
	#Switch Case Ersatz
	if inputVar == "0":			#Zum Terminal zurückkehren
		sys.exit(0)
	elif inputVar == "1":		#Domain/Workgroup
		print("NNN")
	elif inputVar == "2":		#Computername
		print("NNN")
	elif inputVar == "3":		#User hinzufügen
		print("NNN")
	elif inputVar == "4":		#Remotezugriff
		print("NNN")
	elif inputVar == "5":		#Update einstellungen
		print("NNN")
	elif inputVar == "6":		#System updaten
		print("NNN")
	elif inputVar == "7":		#Netzwerkeinstellungen
		networkMenue()
	elif inputVar == "8":		#Datum- und Uhrzeiteinstellung
		print("NNN")
	elif inputVar == "9":		#Tools Einstellungen
		instMenue()
	elif inputVar == "10":		#Abmelden
		logoff()
	elif inputVar == "11":		#Server Neustart
		restart()
	elif inputVar == "12":		#Server Herunterfahren
		shutdown()
	else:						#Wenn etwas anderes eingegeben wurde
		x = input("Falsche eingabe!")
		
	
	#Ruft danach wieder das Hauptmenü auf, ersetzt loop
	menue()
	
#Aufruf Hauptmenü, darf erst nach der Funktion stehen!
menue()