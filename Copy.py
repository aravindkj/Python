from abaqus import *
from abaqusConstants import *
from odbAccess import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import meshEdit
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior



import fileinput, string, sys
from time import sleep

import xml.parsers.expat
import random
import math
from odbAccess import *
import numpy as np
import pprint
import csv


# face = ['TOP','BOTTOM','BOTTOMLEFT','BOTTOMRIGHT','TOPLEFT','TOPRIGHT']
globalCoord = []
globalDispl = []
localCoord=[]
face = ['TOP'] #name of face sets
for fac in face:  # Displacement and Coordinate values of each face(nodeset) is stored in seperate csv file  
    f = open( str(fac)+'.csv', 'rU' ) 
    for line in f:
        cells = line.split( "," )
        globalCoord.append( ( cells[ 0 ], cells[ 1 ], cells[ 2 ] ) ) #Appending global Coordinate values 
        globalDispl.append( ( cells[ 3 ], cells[ 4 ], cells[ 5 ] ) ) #Appending global displacement values 




    # 'bottom','topleft','topright','bottomleft','bottomright'

    localnode=mdb.models['Model-1'].rootAssembly.sets[str(fac)].nodes  #name of face's node sets

    for nod in mdb.models['Model-1'].rootAssembly.sets[str(fac)].nodes: #Coordinate of each node in local face             localCoord.append(nod.coordinates)
        localCoord.append(nod.coordinates)

    localarray =np.asarray(localCoord,dtype=np.float64) #Local coordinate array
    globalarray = np.asarray(globalCoord,dtype=np.float64) #Global coordinate array
    disparray=np.asarray(globalDispl,dtype=np.float64) #Global displacement array
    # print localarray
    def calculateDistance(x1,x2,y1,y2,z1,z2):
         dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2) #Distance function
         return dist
    # print globalarray

    def calculateAverage(d):  # Displacement Average function
        return np.mean(d, axis=0)



    avg=np.array([[]])
    for localrow in localarray:
        # print ("localrow")
        # print (localrow)
        y,x = globalarray.shape
        distancearray = np.zeros(shape=(y,2))
        # print distancearray
        globalindex = 0
        for globalrow in globalarray:
            dist1 = np.linalg.norm(localrow-globalrow)
            # print dist1        
            # print globalindex
            distancearray[globalindex] = [globalindex,dist1]

            globalindex = globalindex+1
        distancearray = distancearray[distancearray[:,1].argsort()] #sorting based on minimum distances
        selectdisparray = np.zeros(shape=(4,3))
        distanceindex = 0
        for distancerow in distancearray[0:4,:]:
            selectdisparray[distanceindex] = disparray[distancerow[0]] #4 minimum distance values
            # print disparray[distancerow[0]]
            distanceindex = distanceindex + 1
        print ("displacement array (for the corresponding points)")    
        print selectdisparray
        print ("the average")
        

    #     calavg=np.array(calculateAverage(selectdisparray))
    #     print calavg
    #     avg=np.append(avg, calavg)
    # avg = np.reshape(avg,(np.size(avg)/3,3))


    # print avg
    for nodal in range(0,len(localnode)):
            region=mdb.models['Model-1'].rootAssembly.Set(name=str(fac)+str(nodal), nodes=
                            mdb.models['Model-1'].rootAssembly.sets[str(fac)].nodes[nodal:nodal+1])
            
            

            mdb.models['Model-1'].DisplacementBC(name=str(fac)+'-'+str(nodal), createStepName='Step-1', 
                region=region, u1=avg[nodal][0], u2=avg[nodal][1], u3=avg[nodal][2], ur1=UNSET, ur2=UNSET, ur3=UNSET, 
                amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
