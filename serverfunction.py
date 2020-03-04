#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os			#für Betriebssystemfunktionen (z.B. exit)

def logoff():		#Funktion für das Abmelden des Users
	os.kill(os.getppid(), 9)

def restart():		#Funktion für den neustart des Servers
	os.system('reboot')

def shutdown():		#Funktion für das herunterfahren des Servers
	os.system("poweroff")