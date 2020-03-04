#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from functions import *

def main():
	clear()
	print()
	print(" ##############################")
	print("          Git-Tool")
	print(" ##############################")
	
	print()
	print(" 0) Zurück")
	
	print()
	print(" 1) Pull from Git")
	print(" 2) Push to Git (Master)")
	
	
	print()
	
	inputVar = input(":")
	if inputVar == "0":
		exit()
	elif inputVar == "1":
		pull()
	elif inputVar == "2":
		push()
	else:
		input("Fehlerhafte Eingabe!")
	main()


def pull():
	os.system("git pull origin master")

def push():
	committext = input("Commit-Name: ")
	
	os.system("git add --all")
	os.system('git commit -m "' + committext + '"')
	
	inputVar = input("Diese Dateien Hochladen? (n/y[std]): ")
	if inputVar == "no":
		return
	elif inputVar == "n":
		return
	
	
	os.system("git push origin master")
	
	print()
	input("Fertig!...")

main()