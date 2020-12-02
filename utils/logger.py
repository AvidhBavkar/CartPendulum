# -*- coding: utf-8 -*-
"""
Logger Program.
"""
from datetime import datetime

kLogFileAddress = "logs/"
kLogFileType = ".csv"
kDelimeter = ','

content = [] #List to contain data
dataHeader = [] #List to contain data headers

def setHeaders(header):
    global dataHeader
    
    dataHeader = header
    
def log(data):
    global contentTuple
    
    content.append(data);
    
def publish(filename, appendDate):
    filename = kLogFileAddress + filename
    if (bool(appendDate)):
        filename += datetime.now().strftime("_%Y%m%d_%H%M%S")
        
    with open(filename, 'w') as f:
        f.write(getLogString())

def getLogString():
    logString = ""
    
    #Add the headers to the top row
    for header in dataHeader:
        if logString != "":
            header = kDelimeter + header
        
        logString += header
    logString += "\n"
    
    for entry in content:
        
        counter = 0
        while (counter < len(entry)):
            logString += str(entry[counter])
            
            if(counter < len(entry) - 1):
                logString += kDelimeter
            counter += 1
        logString += "\n"
        
    return logString

