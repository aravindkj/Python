

import scipy
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

import csv
import sys

# INTREST = ['TOP','BOTTOM','BOTTOMLEFT','BOTTOMRIGHT','TOPLEFT','TOPRIGHT']
odb=openOdb(path='cube.odb')

INTREST = ['TOP']
for nod in INTREST:
	regionofinterest=odb.rootAssembly.nodeSets[str(nod)]

	displacement=odb.steps['Step-1'].frames[-1].fieldOutputs['U']
	coordinates=odb.steps['Step-1'].frames[-1].fieldOutputs['COORD']

	disp=displacement.getSubset(region=regionofinterest)
	coord=coordinates.getSubset(region=regionofinterest)
	dispvalues=disp.values
	coordvalues=np.array(coord.values)


	# df = pd.DataFrame({"name1" : a, "name2" : b})
	# df.to_csv("submission2.csv", index=False)

	print 'disp', len(dispvalues)
	print 'coord', len(coordvalues)
	thefile = open(str(nod)+'.csv', 'wb')

	for i in range(len(dispvalues)):
		for j in range(3):
			du = coordvalues[i].data[j]
			
			thefile.write(str(du) + ',')
		for j in range(3):
			u = dispvalues[i].data[j]
			thefile.write(str(u) + ',')
		thefile.write(''+ '\n')
	thefile.close()





