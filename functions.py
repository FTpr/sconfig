#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os				#für Konsolenfunktion
import platform			#für Systeminformationen

from colors import *	#für Farben

#Bildschirm löschen
def clear():
	if platform.system() == "Linux":
		clear = lambda: os.system('clear') 	#auf Linux System
		clear()
	elif platform.system() == "Windows":
		clear = lambda: os.system('cls') 	#auf Windows System
		clear()

#Checken ob die Datei existiert	(Dateiname)
def fileExists(filename):
	try:
		f = open(filename)	#Versuchen die Datei zu lesen
		return True			#Erfolg zurückgeben
	except IOError:
		return False		#Misserfolg zurück geben


#Farbige Zeile Schreiben (Text als String, color als colors.COLOR)
def printColored(text, color):
	print(color + text + colors.RESET)


#Prüfen ob der Dienst aktiv ist (vollständiger Prozessname)
def checkForProcess(processname):
	tmp = os.popen("ps -Af").read()
	proccount = tmp.count(processname)
	
	if proccount > 0:
		return True
	return False