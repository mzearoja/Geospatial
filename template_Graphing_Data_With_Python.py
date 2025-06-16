#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 01:13:01 2020
@author: kong44

Program description: 
This program accepts text files and generates summary figures of the data. 
Text files have been provided by the instructor, it is data from bodies of water. 
"""

# importing modules

import numpy as np
import matplotlib.pyplot as plt
from io import StringIO


def read_data( inFileName ):
    '''Uses NumPy genfromtxt to open inFileName and generate data array with 
    header names corresponding to the columns names in the file.  Returns the
    resulting data structure to the main code.'''    
    with open(inFileName, 'r') as f2:
        lines = f2.readlines()
        
        data = []# define data as a list 
        for line in lines:
            p = line.split()
            data.append(p)
        data = [line.split() for line in lines] #in one comand
        print(data[0])
        data2 = np.array(data)
        print(data2.shape)
        data2= np.genfromtxt(inFileName, dtype=("str"), usecols = [0, 1, 2, 3, 4, 5, 6])
        for i in range(100):
            for j in range(2):
                return data
    
    # with open(inFileName, 'r') as f:
    #     lines = [line for line in f]
    # if len(lines) < 2:
    #     return None
    # keys = [name.strip() for name in lines[0].split(',')]
    # data = np.genfromtxt(inFileName, dtype=("str"), usecols = [0, 1, 2, 3, 4, 5, 6])
    # if data.ndim == 1:
    #     data = data.reshape(1, -1)
    # assert data.ndim == 2
    # assert data.shape[-1] == len(keys)
    # result = {}
    # for idx, key in enumerate(keys):
    #     result[key] = data[:, idx]
    # return result



# data = [line.split() for line in lines] in one comand.
#print(data[0]) #first element of the list data
#data2 = np.array(data)
# print(data2.shape) #to tell the shape of the array
# x = data2[:,0]#o access the distinct columns
# y = data2[:,1]
#z = (data2[:,0]**2 + data2[:,1]**2)**0.5 # As the array is a numpy object, one can perform operations on it
#data3 = np.loadtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt') Numpy includes functions to read ascii files and return float arrays directly.

                     

                      #An even more complete tool to read ascii file
##One can even ask for this function to automatically put the result in 2 different variables:
#x, y = np.loadtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', unpack = True)
#x, y = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', unpack = True)
#read using this command:

        
#The skip_header tells not to read the first line. The dtype describes the type of the 6 columns. delimiter is the list of the sizes (in characters) of each column. The names are used to identify the columns. The usecols is used to specify which columns to output (here I don't need the 5th column, made of 2 spaces before the observer name)


def plot_data( plotData, outFileName ):
    '''Uses matplotlib module to generate a single page figure with three 
    panels.  Accepts the data structure from read_data and the name of an
   outputfile, and generates a PDF file with the figure.'''

   

    
    '''Use this part of the program to prompt the user for the name of the 
    datafile to print, and then read in the contents of that file, and produce
    a plot matching the assignment requirements.'''
   
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    
    inFileName = 'Tippecanoe_River_at_Ora.Annual_Metrics.txt'
    #inFileName = 'Wildcat_Creek_at_Lafayette.Annual_Metrics.txt'
    DataDic = read_data( inFileName )
    plt.savefig('foo.png')
    plt.savefig('foo.pdf')

    


