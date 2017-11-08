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



globalCoord = []
globalDispl = []
localCoord=[]

f = open( 'test1.csv', 'rU' ) 
for line in f:
    cells = line.split( "," )
    globalCoord.append( ( cells[ 0 ], cells[ 1 ], cells[ 2 ] ) ) 
    globalDispl.append( ( cells[ 3 ], cells[ 4 ], cells[ 5 ] ) )

localnode=mdb.models['Model-1'].rootAssembly.sets['local'].nodes

for nod in mdb.models['Model-1'].rootAssembly.sets['local'].nodes:
        localCoord.append(nod.coordinates)


localarray =np.asarray(localCoord,dtype=np.float64)
globalarray = np.asarray(globalCoord,dtype=np.float64)
disparray=np.asarray(globalDispl,dtype=np.float64)


def calculateDistance(x1,x2,y1,y2,z1,z2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2)
     return dist
# print globalarray

def calculateAverage(d):
    return np.mean(d, axis=0)

ranNodes=range(0,len(localnode))
repConst=0

for repnod1 in range(0,len(localnode)):
    
    Coor1=localCoord[repnod1]

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
        print distancearray
        for distancerow in distancearray[0:4,:]:
            
            selectdisparray[distanceindex] = disparray[distancerow[0]]
            # print disparray[distancerow[0]]
            distanceindex = distanceindex + 1
            thenode=localrow       

            # avg=[]
            average=calculateAverage(selectdisparray)
        # avg.append(average)
        
    
        # print average,repnod1
    # region=mdb.models['Model-1'].rootAssembly.Set(name='Node-1-'+str(repnod1), nodes=
    #        mdb.models['Model-1'].rootAssembly.sets['local'].nodes[repnod1:repnod1+1])

    # mdb.models['Model-1'].DisplacementBC(name='load'+'-'+str(repnod1), createStepName='Step-1', 
    #     region=region, u1=avg[0][0], u2=avg[0][1], u3=avg[0][2], ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    #         amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

    #             # print repnod1   

    # for i in avg:
    #     del i
    # print "deleted"
    # print avg[0]
        # # print "step"
        # print localrow
        # repnod=repnod+1 #Increase integer for naming equation constraint
      