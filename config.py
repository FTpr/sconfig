#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import * 	#für wichtige Funktionen
from colors import *

fehlermeldung = ""

def instMenue():
	global trysDHCP, fehlermeldung		#Globale Variable lokal verfügbar machen
	trysDHCP = 0						#Variable wie oft die Installation versucht wurde
	
	clear()								#Display leeren (aus functions)
	print()
	print("=========================================================")
	print("               Zusatzsoftware konfigurieren")
	print("=========================================================")
	print()
	
	print(" 0) Zurück")
	print()
	
	statusColor = colors.RESET					#Zeilenfarbe zurücksetzen
	
	if not fehlermeldung == "":					#Wenn eine Fehlermeldung übergeben wurde
		printColored(fehlermeldung, colors.RED)		#Fehlermeldung in rot Schreiben
		print()										#Leerzeile einfügen
		fehlermeldung = ""							#Fehlermeldung zurücksetzen
	
	if checkForDHCP():							#Prüfen ob DHCP installiert ist
		statusColor = colors.GREEN				#Zeilenfarbe auf grün ändern
	printColored(" 1) DHCP (Automatische Adressverteilung)", statusColor)		#Zeile schreiben
	statusColor = colors.RESET
	
	
	if checkForDNS():							#Prüfen ob DNS installiert ist
		statusColor = colors.GREEN				#Zeilenfarbe auf grün ändern
	printColored(" 2) DNS  (Namensauflösung)", statusColor)		#Zeile grün schreiben
	statusColor = colors.RESET
	
	
	if checkForSamba():							#Prüfen ob SAMBA installiert ist
		statusColor = colors.GREEN				#Zeilenfarbe auf grün ändern
	printColored(" 3) SMB  (Ordnerfreigabe)", statusColor)		#Zeile grün schreiben
	statusColor = colors.RESET
	
	
	if checkForFtp():							#Prüfen ob FTP installiert ist
		statusColor = colors.GREEN				#Zeilenfarbe auf grün ändern
	printColored(" 4) FTP  (Dateiserver)", statusColor)		#Zeile grün schreiben		
	statusColor = colors.RESET
	
	
	print()
	print(" 5) HTTP (Web-Server)")
	print(" 6) Mail-Server (Senden)")
	print(" 7) Mail-Server (Empfangen)")
	
	
	
	#auf Eingabe warten
	inputVar = input(":")
	
	#Switch Case Ersatz
	if inputVar == "0":		#Zurück zum Hauptmenü
		return						#Funktion Tools-Menü beenden
	elif inputVar == "1":			#Auswahl DHCP
		menueDHCP()
	elif inputVar == "2":		#Auswahl DNS
		menueDNS()
	elif inputVar == "3":		#Auswahl SMB
		print("NNN")
	elif inputVar == "4":		#Auswahl FTP
		print("NNN")
	elif inputVar == "5":		#Auswahl Webserver
		print("NNN")
	elif inputVar == "6":		#Auswahl Mail-Send
		print("NNN")
	elif inputVar == "7":		#Auswahl Mail-Empfang
		print("NNN")
	
	else:						#Wenn eine unzulässige Eingabe gemacht wurde
		print("Falsche eingabe!")	#Fehlermeldung
	
	instMenue()		#Das Menü wieder neu aufbauen


#	Bereich DHCP
#---------------
def checkForDHCP():		#Ist der Dienst installiert?
	return checkForProcess("dhcp")
	
def menueDHCP():
	global trysDHCP, fehlermeldung		#Globale Variable lokal verfügbar machen
	
	clear()
	if checkForDHCP():
		print()
		print(" ------------")
		print("  DHCP-Menü")
		print(" ------------")
		print()
		print(" 1) Neuer Bereich")
		print(" 2) ")
		print(" 3) Deinstallieren")
		print()
		print(" 4) Zurück")
		print()
		
		inputVar = input(":")	#auf Eingabe warten
		if inputVar == "1":		#Neuen bereich erstellen
			print()
		elif inputVar == "4":	#
			print()
		elif inputVar == "3":	#Deinstallieren
			removeDNS()
			return
		elif inputVar == "4":	#Zurück
			return
		else:
			print("Falsche eingabe!")	#Fehlermeldung
	else:
		if trysDHCP == 0:
			installDHCP()
			trysDHCP = trysDHCP + 1
		else:
			fehlermeldung = "DHCP Installation konnte nicht abgeschlossen werden!"
			return
	menueDHCP()


def installDHCP():
	os.system("apt --assume-yes install isc-dhcp-server")	#Konsolenanweisung zum installieren DHCP


def removeDHCP():
	os.system("apt --assume-yes remove isc-dhcp-server")	#Konsolenanweisung zum deinstallieren DHCP


#	Bereich DNS
#---------------
def checkForDNS():		#Ist der Dienst installiert?
	return checkForProcess("bind")
	
def menueDNS():			#DNS-Menü
	clear()
	if checkForDNS():		#Wenn der Dienst bereits installiert ist
		print()				#Menü zeichnen
		print(" ------------")
		print("   DNS-Menü")
		print(" ------------")
		print()
		print(" 1) Bereich konfigurieren")
		print(" 2) ")
		print(" 3) Deinstallieren")
		print()
		print(" 4) Zurück")
		print()
		
		inputVar = input(":")	#auf Eingabe warten
		if inputVar == "1":		#
			print()
		elif inputVar == "2":	#
			print()
		elif inputVar == "3":	#Deinstallieren
			removeDNS()
			return
		elif inputVar == "4":	#Zurück
			return
		else:
			print("Falsche eingabe!")	#Fehlermeldung
	else:
		installDNS()
	menueDNS()


def installDNS():			#Installation DNS-Server + Zubehör
	os.system("apt --assume-yes install bind9")			#Installation mit automatischer Zustimmung DNS-Server
	os.system("apt --assume-yes install dnsutils")		#Installation mit automatischer Zustimmung Hilfswerkzeuge

def removeDNS():			#Deinstallation DNS-Server + Zubehör
	os.system("apt --assume-yes remove bind9")	
	os.system("apt --assume-yes remove dnsutils")


#	Bereich SMB
#---------------
def checkForSamba():		#Ist der Dienst installiert?
	return checkForProcess("smbd")


def menueSamba():			#DNS-Menü
	clear()
	if checkForSamba():		#Wenn der Dienst bereits installiert ist
		print()				#Menü zeichnen
		print(" ------------")
		print("   SMB-Menü")
		print(" ------------")
		print()
		print(" 1) Bereich konfigurieren")
		print()
		
		inputVar = input(":")

def installSamba():			#Samba installieren
	os.system("apt-get --assume-yes install samba")			#Installation mit automatischer Zustimmung Samba-Server


#DARF NICHT AKTIVIERT WERDEN! BEI DEINSTALLATION VON SAMBA KANN DER ZUGRIFF VERLOREN GEHEN!
#def removeSamba():			#Samba deinstallieren
#	os.system("apt-get --assume-yes remove samba")			#Deinstallation mit automatischer Zustimmung Samba-Server



#	Bereich FTP
#---------------

def checkForFtp():			#Ist der Dienst installiert?
	return checkForProcess("sftpd")
