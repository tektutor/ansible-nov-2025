#!/usr/bin/python3

def writeToFile( fileName, message ):
    file = open(fileName, "a")
    file.write(message+"\n")
    file.close()

def readFile( fileName ):
    file  = open(fileName, "r")

    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
    file.close()

writeToFile( "cars.txt", "Honda City" )
writeToFile( "cars.txt", "Skoda Kodiaq" )
writeToFile( "cars.txt", "Audi A6" )

readFile( "cars.txt" )
