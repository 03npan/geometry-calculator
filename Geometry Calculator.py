# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:01:20 2018

@author: Nathan
"""
# Nathan Pan
# 7/10/2018
# Purpose: Geometry calculator using programmer-defined functions, while loops, and if/elif/else statements

#CUBE VOLUME
def calcCubeVol(side):
    vol = pow(side, 3)
    return vol
    print(vol)

#CUBE SURFACE AREA
def calcCubeSA(side):
    surfaceArea = 6 * pow(side, 2)
    return surfaceArea
    print(surfaceArea)

#TRIANGLE AREA
def calcTrigArea(base, height):
    area = (1/2) * base * height
    return area
    print(area)

#TRIANGLE PERIMETER
def calcTrigPerim(side1, side2, side3):
    perim = side1 + side2 + side3
    return perim
    print(perim)

#MENU OBSOLETE NOW, JUST HERE SO MAIN FUNCTION WORKS RIGHT NOW
def showMenu():
    print("1. Cube Volume")
    print("2. Cube Surface Area")
    print("3. Triangle Area")
    print("4. Triangle Perimeter")
    print("5. Quit")
    userChoice = input("Make a selection:")
    return userChoice

def mainMenu():
    print("1. Perimeter")
    print("2. Area")
    print("3. Volume")
    print("4. Surface Area")
    print("5. Quit")
    userChoice = input("Make a selection:")
    return userChoice

def perimeterMenu():
    print("Perimeter")
    print("-------------------------------")
    print("1. Circle")
    print("2. Regular polygon")
    print("3. Back")
    
def areaMenu():
    print("Area of regular polygons")
    print("-------------------------------")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Pentagon")
    print("5. Hexagon")
    print("6. Octagon")
    print("7. Decagon")
    print("8. Circle")
    print("9. Back")
   
def volumeMenu():
    print("Volume of regular solids")
    print("-------------------------------")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    
def surfaceAreaMenu():
    print()

def main():
    userChoice = showMenu()
    while (userChoice != "5"):
      if userChoice == "1":
        side = float(input("Enter side length:"))
        print("The volume is " + str(calcCubeVol(side)) + ".")
        print("")
      elif userChoice == "2":
        side = float(input("Enter side length:"))
        print("The surface area is " + str(calcCubeSA(side)) + ".")
        print("")
      elif userChoice == "3":
        base = float(input("Enter base:"))
        height = float(input("Enter height:"))
        print("The area is " + str(calcTrigArea(base, height)) + ".")
        print("")
      elif userChoice == "4":
        side1 = float(input("Enter length of side 1:"))
        side2 = float(input("Enter length of side 2:"))
        side3 = float(input("Enter length of side 3:"))
        print("The perimeter is " + str(calcTrigPerim(side1, side2, side3)) + ".")
        print("")
      else:
        #ANYTHING NOT ACCEPTED INPUT
        print("Please select either 1, 2, 3, 4, or 5.")
        print("")
      userChoice = showMenu()

main()