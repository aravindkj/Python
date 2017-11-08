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
face = ['TOP']
for fac in face:    
    f = open( str(fac)+'.csv', 'rU' ) 
    for line in f:
        cells = line.split( "," )
        globalCoord.append( ( cells[ 0 ], cells[ 1 ], cells[ 2 ] ) ) 
        globalDispl.append( ( cells[ 3 ], cells[ 4 ], cells[ 5 ] ) )




    # 'bottom','topleft','topright','bottomleft','bottomright'

    localnode=mdb.models['Model-1'].rootAssembly.sets[str(fac)].nodes

    for nod in mdb.models['Model-1'].rootAssembly.sets[str(fac)].nodes:
            localCoord.append(nod.coordinates)


    localarray =np.asarray(localCoord,dtype=np.float64)
    globalarray = np.asarray(globalCoord,dtype=np.float64)
    disparray=np.asarray(globalDispl,dtype=np.float64)
    # print localarray
    def calculateDistance(x1,x2,y1,y2,z1,z2):
         dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2)
         return dist
    # print globalarray

    def calculateAverage(d):
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
            # check stackoverflow first
            # dist2 = calculateDistance(
            #     localrow[0],globalrow[0],
            #     localrow[1],globalrow[1],
            #     localrow[2],globalrow[2]
            #     )
            # print dist2
            # print (dist1==dist2)
            globalindex = globalindex+1
        distancearray = distancearray[distancearray[:,1].argsort()]
        # now the distancearray is sorted
        # print ("distance array (point index, distance)")
        # print distancearray[0:4,:]
        selectdisparray = np.zeros(shape=(4,3))
        distanceindex = 0
        for distancerow in distancearray[0:4,:]:
            selectdisparray[distanceindex] = disparray[distancerow[0]]
            # print disparray[distancerow[0]]
            distanceindex = distanceindex + 1
        # print ("displacement array (for the corresponding points)")    
        # print selectdisparray
        # print ("the average")

        calavg=np.array(calculateAverage(selectdisparray))
        avg=np.append(avg, calavg)
    avg = np.reshape(avg,(np.size(avg)/3,3))


    print avg
    for nodal in range(0,len(localnode)):
            region=mdb.models['Model-1'].rootAssembly.Set(name=str(fac)+str(nodal), nodes=
                            mdb.models['Model-1'].rootAssembly.sets[str(fac)].nodes[nodal:nodal+1])
            
            

            mdb.models['Model-1'].DisplacementBC(name=str(fac)+'-'+str(nodal), createStepName='Step-1', 
                region=region, u1=avg[nodal][0], u2=avg[nodal][1], u3=avg[nodal][2], ur1=UNSET, ur2=UNSET, ur3=UNSET, 
                amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
