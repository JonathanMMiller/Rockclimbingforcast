import pandas as pd
import climbclass

NorB = climbclass.ClimbLocation("North Bend Exit 32/38", 47.49, -121.78)
LaC = climbclass.ClimbLocation("Lake Cushman",47.499,-123.291)
# Van = climbclass.ClimbLocation("Vantage",47.025,-119.967)
# GdB = climbclass.ClimbLocation("Gold Bar",47.845,-121.627)
# LnW = climbclass.ClimbLocation("LeavenWorth",47.545,-120.734)
# Sqm = climbclass.ClimbLocation("Squamish",49.687,-123.136)
# SRk = climbclass.ClimbLocation("Smith Rock",44.363,-121.146)
# Maz = climbclass.ClimbLocation("Mazama", 48.608,-120.401)
# Tet = climbclass.ClimbLocation("Tieton River", 46.724,-120.809)
# MtE = climbclass.ClimbLocation("Mount Erie", 48.460, -122.625)

# temporary but is a list of Variables to For loop class methods
Var_Dict = {'NorB':NorB, 'LaC':LaC}
            # 'Van': Van,'GdB': GdB, 'LnW': LnW, 
            # 'Sqm': Sqm, 'SRk': SRk, 'Maz':Maz, 'Tet':Tet, 'MtE':MtE}
           # Van, GdB, LnW, Sqm, SRk, Maz, Tet, MtE]
Df_dict = Var_Dict

for i, var in Df_dict.items():
  Df_dict[i] = pd.DataFrame(var.requestforcast(),).T
  print(Df_dict[i])

  #gotta send somewhere here or figure out a way to save each DataFrame to a unique list variable
       
# print(data)
#   all_data= pd.concat([data,all_data], axis =0)
  
# AlldataT=all_data.T
# AlldataT.to_csv('Forcastall.csv)
# # print(len(all_data))

# print(Var_List)
# print(NorB.name, NorB.lat, NorB.lon, NorB.getaccumrain())
#creates class instance object from class ClimbLocation from climbclass.py
#user inputs name, latidude and longitude

#List of stuff to do

#Task 1
# Make an index list of the variables for class instances
# Run the list and compile data into a large data frame
# export data to excel or format
