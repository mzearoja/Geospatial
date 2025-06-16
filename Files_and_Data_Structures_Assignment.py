#!/usr/bin/env python
"""
@maria Zea  Homework No. 3


Program read  .txt file, and stored file data into a dictionary
functions defined  using the columns of the data. 
new outfile named George's life. txt' is written


assignments: George's_life.txt with metadata


"""
yes 

#import packages

import statistics 
import math
import os

## first define dictionary and read it

def read_data_file (fileName):
     fileName = open( fileName, "r" ) #r is for reading
     lines = fileName.readlines()     ## read all data
     print (fileName) ## see data
     fileName.close()## better to close it
     
#      Var1 = filename.read(45) # 45 bytes usedvar 1 are printed you can see that it contains the first line and part of the second line of the file.
# #     print ( Var1 )
#      filename.seek(0) #returns the file pointer (fin) to the start of the file.
#      Var2 = filename.readline() # reads the file until it reaches an end-of-line or end-of-file marker and returns a string.
# #     print ( Var2 )
#      Var3 = filename.readlines() # read file until it encounters an end-of-file marker and returns a list of strings, where each string represents a lines in the file
# #     print ( Var3 )   
#      filename.close()
     

# data structure framwork. 
    
     header = lines[0].split(',') #build header get strings from the data
     for i in range(len(header)): 
         header[i] = header[i].strip()
        
        ##Dictionary
     Data = dict.fromkeys(header, []) # empty data dictionary
    
     
    #biuld dictionary values:
         
     Nlines = len(lines) 
     for lidx in range(1,Nlines-1): # process all data lines in the file 
        tmpVar = lines[lidx].strip().split(',') # get all data from current line 
        for col in range(len(tmpVar)): # loop through all data values on current line  
            Data[header[col]] = Data[header[col]] + [tmpVar[col]] # append current value to end of dictionary list

#assing and formart animal status
     Data['Status'] = lines[-1].strip()

#format table values 
     for lidx in range(1,Nlines-1):
# from list data assign float data and table values
      Data ['X'] = list(map(float, Data['X'])) #dictionary keys ## x value 
      Data ['Y'] = list(map(float, Data['Y']))
      
      Data ['Energy Level'] = list(map(float,Data['Energy Level'])) 
      return Data
    

         

# # define required descriptive caluclations here

#define mean

def compute_mean(value_list):
     ''' Computes average of a list, and returns that value. '''

     avg = statistics.mean(value_list) # using statistic package
     return avg # return to value

def compute_sum(value_list):
     ''' Computes cumulative sum of a list, and returns that value. '''  
     Comp_sum = sum(value_list)
     return Comp_sum # return cumulative sum
    
# #   return pipe(cmd)

#define function

def distance_between_points(x1,y1,x2,y2):
     
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)) 
      
    return distance
  
    ## using data Dic for following data
dataDict = read_data_file('2008Male00006.txt')        
  
def compute_distance_traveled(X, Y):
#      ''' Computes the distance between each subsequent set of coordinates from 
#     two lists, X and Y coordinates of the raccoon.  Function returns list of 
#     distances added to dictionary, with initial distance = 0. List should be 
#     the same length as the input X and Y lists.'''  
 
    distance = [0]
    
    for n in range (len(dataDict['X'])-1):
    
        dist_travel = distance_between_points(dataDict['X'][n], dataDict['Y'][n],
                                              dataDict['X'][n+1], dataDict['Y'][n+1])## equation
        
        distance.append((dist_travel)) # append value
    
  
    return distance ## returning to function
    
  
        

# # define function to read in the contents of the given data file, convert
# # columns to appropriate numerical values (as needed), and create a data
# # structure for processing using a dictionary.  The dictionary should be
# # returned to the main code for later use.
# #
# # - dictionary keys should not include white space.
# # - dictionary items should be named for column headers, and include data for 
# #   that column converted to the appropriate numerical format, if appropriate.
# # - end status of the raccoon should be stored in the data dictionary under 
# #   the keyword 'Status'

# def read_data_file( fileName ):


# # include a function to output the reformatted data file.
# # Output file should have a header that includes:
# # Raccoon name: <name of the raccoon> 
# # Average location: X <average X position>, Y <average Y position>
# # Distance traveled: <total distance traveled>
# # Average energy level: <average energy level>
# # Raccoon end state: <string indicating final raccoon status>
# #
# # The header should be followed by a blank line, then the following headers
# # prviding a starting point for a tab delimited table of data values:
# # - Date, X, Y, Asleep Flag, Behavior Mode, Distance Traveled
# # - subsequent lines should be the relevent values for each header category
# #   separated by tabs.

 
    
def write_output_file (outName, dataDict, avg_energy, avg_x, avg_y, t_dist): 
    outFile = open('outName', 'w')   # w is for writing 
    outFile .write('My first output file!') ## title
    outFile .write('') # blank
    #outFile.close()
         
# # the following condition checks whether we are
# # running as a script, in which case run the test code,
# # or being imported, in which case don't.


     # writting header
    outFile.write('Racoon name: {}\n'.format(dataDict['Status'][0:6])) ## first header 
    outFile.write('Average energy level {}\n'.format(avg_energy))
    outFile.write('Average location: {},{}\n'.format(avg_x , avg_y))   
    outFile.write('Distance traveled: {}\n'.format(t_dist))   
    outFile.write('Racoon end state: {}\n'.format(dataDict['Status']))
    
    # write a blank
    outFile.write('')
        
    # writting header lables helps to organize data
    header = ['Date', 'Time', 'X', 'Y', 'Asleep', 'Behavior Mode', 'Distance Traveled']
    outFile.write('{}\n'.format('\t'.join(header)))
    
    # write contents of data dictionary
    for row in range(len(dataDict['Day'])):
        outFile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\n'.format(dataDict['Day'][row], dataDict['Time'][row], dataDict['X'][row],
                                                             dataDict['Y'][row], dataDict['Asleep'][row], dataDict['Behavior Mode'][row],
                                                             dataDict['Distance'][row])) ## wrote 7 columns
    outFile.close()## impornt : always close the file
     
if __name__ == '__main__':
    
        # set input and output file names

     inFile = '2008Male00006.txt'
     outFile = "Georges_life.txt" 
     
    # read input file
     dataDict = read_data_file(inFile)## read dictionary data
     print (dataDict)
#     # write output data to a file
    
#     #write_output_file( outFile, dataDict, avg_energy, avg_x, avg_y, t_dist )

    # calling all funcitions defined above
     dataDict['Distance'] = compute_distance_traveled(dataDict['X'], dataDict['Y']) 
 
     avg_energy = compute_mean(dataDict['Energy Level']) #avgerage energy
     avg_x = compute_mean(dataDict['X']) # average x location
     avg_y = compute_mean(dataDict['Y']) # average y location
     t_dist = compute_sum(dataDict['Distance']) # total distance traveled
     
     name = (dataDict['Status'][0:6])
     
         # write output data to txt file
     write_output_file( outFile, dataDict, avg_energy, avg_x, avg_y, t_dist )
    








