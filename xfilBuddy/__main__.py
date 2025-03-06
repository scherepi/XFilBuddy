# XFilBuddy - Your new favorite exfiltration tool! Take me all over your systems - I want to see the world...
# Created in March of 2025 by John Vincent Moon - Travel wary, lest you should stumble into a garden of ever-forking paths

# Imports
import argparse
import random
import sys
import socket
from XFilServer import XFilServer

def printBanner():
    print("########################################################################")
    print("##                                                                    ##") 
    print("##                i know the first three numbers...                   ##")
    print("##                                                                    ##")
    print("### # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##")
    #TODO: add randomized banners

def printStartMenu():
    print(">> Welcome to XFilBuddy.. are you stealing shit or receiving stolen shit? <<")
    print("1. Start up an XFilBuddy")
    print("2. Prep an XFilServer")
    print("3. Exit")
    print("Enter your choice: ")
    chosenInput = input()
    while (chosenInput != "1" and chosenInput != "2" and chosenInput != "3"):
        print("Don't waste my time, dumbass. That's not a valid answer.")
        chosenInput = input()
    return chosenInput

def clientChosen():
    # Main logical branch for when the user selects to begin an XFilBuddy client.
    options = []

def serverChosen():
    # Main logical branch for when the user selects to begin an XFilServer
    options = []
    server = XFilServer("nevermind", "hehe")
    server.sayHello()


def __main__():
    printBanner()
    menuSelection = printStartMenu()
    if (menuSelection == "1"):
        clientChosen()
    elif (menuSelection == "2"):
        serverChosen()
    else:
        print("Hate to see you go, love to watch you walk away.")
        exit(0)




__main__()