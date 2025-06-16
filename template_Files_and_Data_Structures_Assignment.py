
#!/usr/bin/env python
"""
Update with your header information


"""



# Filename = open ("2008Male00006.txt")
# lines = Filename.readlines()
# print(Filename)

# for key, value in zip(key_list, value_list):
#     mapping[key] = value

# mapping = {}

# for i, v in enumerate(some_list):
#     mapping[v] = i

# mapping

import statistics
import math
# # import required modules here

# # define required descriptive caluclations here

def compute_mean(value_list):
     ''' Computes average of a list, and returns that value. '''
     for key, value in zip(key_list, value_list):
         mapping[key] = value 
         mapping = {} 
         for i, v in enumerate(some_list): 
             mapping[v] = x
     avg = statistics.mean((value_list))
     return avg

def compute_sum(filename):
     ''' Computes cumulative sum of a list, and returns that value. '''  
     cmd = 'sum ' + filename
     return (cmd)
    
# #   return pipe(cmd)


def distance_between_points(x1,y1,x2,y2):
      ''' Computes the distance between two sets of coordinate points (x1,y1) 
      and (x2,y2), and that value.  '''
      distance = math.sqrt( ((x1[0]-y1[0])**2)+(x2(1[1]-y2[1])**2) ) 
      return (distance)
     
     
     
def compute_distance_traveled(X, Y):
    ''' Computes the distance between each subsequent set of coordinates from 
#     two lists, X and Y coordinates of the raccoon.  Function returns list of 
#     distances added to dictionary, with initial distance = 0. List should be 
#     the same length as the input X and Y lists.''' 
def compute_distance_traveled(X, Y):
     ''' Computes the distance between each subsequent set of coordinates from 
    two lists, X and Y coordinates of the raccoon.  Function returns list of 
    distances added to dictionary, with initial distance = 0. List should be 
    the same length as the input X and Y lists.''' 
    distance = [0] 
    for n in range (len(dataDict['X'])-1):
    
        dist_travel = distance_between_points(dataDict['X'][n], dataDict['Y'][n],
                                              dataDict['X'][n+1], dataDict['Y'][n+1])
        
        distance.append((dist_travel))
    
  
        

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


def read_data_file (filename):
     filename = open( filename, "r" ) 
     lines = filename.readlines()     
     print (filename) 
     
     Var1 = filename.read(45) # 45 bytes usedvar 1 are printed you can see that it contains the first line and part of the second line of the file.
#     print ( Var1 )
     filename.seek(0) #returns the file pointer (fin) to the start of the file.
     Var2 = filename.readline() # reads the file until it reaches an end-of-line or end-of-file marker and returns a string.
#     print ( Var2 )
     Var3 = filename.readlines() # read file until it encounters an end-of-file marker and returns a list of strings, where each string represents a lines in the file
#     print ( Var3 )   
     filename.close()
     

# data structure framwor
     header= lines[0].strip(',')

     Data = dict.fromkeys(header, []) # empty data dictionary

     Nlines = len(lines) 
     for lidx in range(1,Nlines-1): # process all data lines in the file 
        tmpVar = lines[lidx].strip().split(',') # get all data from current line 
        for col in range(len(tmpVar)): # loop through all data values on current line  
            Data[header[col]] = Data[header[col]] + [tmpVar[col]] # append current value to end of dictionary list

#assign and formart animal status
     Data ["status"]= lines[-1].strip()

#format table values 
     for lidx in range(1,Nlines-1):
         Data['Energy Level'] = map(float,Data['Energy Level'])
         Data[lidx][4:6]= map(float,Data[lidx][4:6])
         Data[lidx][6:8] = map(str,Data[lidx][6:8])
         Data[lidx][8]= float(Data[lidx][8]) 
         EnergyLevel = map(float,Data['Energy Level'])
         Data['Energy Level'] = map(float,Data['Energy Level'])
     return Data
 
    
def write_output_file( outName, dataDict, avg_energy, avg_x, avg_y, t_dist ):
      ''' outName is a string defining the name of the output file
        dataDict is the data dictionary first created by read_data_file
        avg_energy is a single value of the average energy used
         avg_x is a single value of the average x-position
         avg_y is a single value of the average y-poisition
         t_dist is a single value of the total distance traveled''' 
   
     
# # the following condition checks whether we are
# # running as a script, in which case run the test code,
# # or being imported, in which case don't.

if __name__ == '__main__':
   


     # set input and output file names
     inFile = '2008Male00006.txt'
     outFile = "Georges_life.txt"

     # read input file
     # dataDict = read_data_file(inFile)
     #         for val in collection: 
     #        if condition: 
     #            result.append(expr)
         
     #     f key in some_dict:
     #         value = some_dict[key] 
     #         else: 
     #             value = default_value


     # complete summary calculations
     compute_mean(print)
     # compute_sum(print)
     # distance_between_points (print)
     
     
#     # write output data to a file
#     #write_output_file( outFile, dataDict, avg_energy, avg_x, avg_y, t_dist )
