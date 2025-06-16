#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:56:59 2020

@author: mpzr44
"""
import statistics


fileName = open ( "2008Male00006.txt", "r" ) 
lines = fileName.readlines()     
fileName.close() # close file

     
#      Var1 = filename.read(45) # 45 bytes usedvar 1 are printed you can see that it contains the first line and part of the second line of the file.
# #     print ( Var1 )
#      filename.seek(0) #returns the file pointer (fin) to the start of the file.
#      Var2 = filename.readline() # reads the file until it reaches an end-of-line or end-of-file marker and returns a string.
# #     print ( Var2 )
#      Var3 = filename.readlines() # read file until it encounters an end-of-file marker and returns a list of strings, where each string represents a lines in the file
# #     print ( Var3 )   
     
     

# data structure framework


Data = [0]*len(lines)

#format table values 
for lidx in range(1,15):
         Data[lidx]= lines[lidx].strip().split('\t')
         Data[lidx][4:6]= map(float, Data[lidx][4:6])
         Data[lidx][6:8] = map(str, Data[lidx][6:8])
         Data[lidx][8]= float(Data[lidx][8])
  
        
header = lines[0].strip.split(',') #header string
Nlines = len(lines) 
Data = {} # creates an empty dictionary with no structure
for lidx in range(1,Nlines-1): # process all data lines in the file 
  tmpVar = lines[lidx].strip().split('\t') # get all data from current line
  if lidx == 1: # handle first line differently
    for col in range(len(tmpVar)): # loop through all data values on current line
      Data[header[col]] = [ tmpVar[col] ] # create key and store first data item as a list
  else:
    for col in range(len(tmpVar)): # loop through all data values on current line
      Data[header[col]].append(tmpVar[col]) # append current value to end of dictionary list
         
Data["Status"] = lines[-1].strip()
         
         #framework
#header = lines[0].strip.split(',') #header string
x

# Nlines = len(lines) 
# Data = dict.fromkeys( header, [] ) # build empty data dictionary
# for lidx in range(1,Nlines-1): # process all data lines in the file 
#   tmpVar = lines[lidx].strip().split(',') # get all data from current line
#   for col in range(len(tmpVar)): # loop through all data values on current line
#       Data[header[col]].append(tmpVar[col])# append current value to end of dictionary lis


# Nlines = len(lines) 
# for lidx in range(1,Nlines-1): # process all data lines in the file 
#         tmpVar = lines[lidx].strip().split(',') # get all data from current line 
#         for col in range(len(tmpVar)): # loop through all data values on current line  
#             Data[header[col]] = Data[header[col]] + [tmpVar[col]] # append current value to end of dictionary list


Data["Status"] = lines[-1].strip()

print [Data]



      
# d = dict (zip(header, body))
# print(d)
     


