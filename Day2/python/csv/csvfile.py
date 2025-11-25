#!/usr/bin/python3

import csv

def writeToCSVFile( filename, name, aadhar ):
    file = open(filename, "a")
    writer = csv.writer(file)
    writer.writerow([name,aadhar])
    file.close()

def readFromCSV( filename ):
    file = open(filename, "r")
    reader = csv.reader(file)
    for row in reader:
        print(row)


writeToCSVFile("aadhar.csv", "Ram", "123412341234")
writeToCSVFile("aadhar.csv", "Rafiq", "834353523524")

readFromCSV( "aadhar.csv" )
