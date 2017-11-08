from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

from abaqus import *
from abaqusConstants import *
from caeModules import *
from odbAccess import *
from numpy import *
import math

odbPath = "D:\SIMULIA\Temp\COMPRESSION_XY-Copy.odb"  
odb = openOdb(path='TENSION_XY-Copy.odb')
grout_instance = odb.rootAssembly.instances['PART-1-1']
numElem = len(grout_instance.elements)
keys = odb.steps.keys()
for stp in keys:
	step = odb.steps[stp]
	# retrieve frames from the odb
	frameRepository = step.frames
	numFrames = len(frameRepository)
	for fr in range(0,numFrames):
		frame=step.frames[fr]
		# print 'Id = %d, Time = %f\n'%(frame.frameId,frame.frameValue)
		# get fieldOutputs object
		fo = frame.fieldOutputs
		S  = fo['S']
		EVOL = fo['EVOL']
		S_grout = S.getSubset(region=grout_instance,\
						position=INTEGRATION_POINT,
						elementType='C3D4')
		EVOL_grout = EVOL.getSubset(region=grout_instance)
		myStress_data = {}
		svalues=[]
		a=S_grout.values


		 #Declaration of my New stress Data
		# Loops over elements to get stpress S11 and Volume
		# for i in range(0,len(S_grout.values)):
		# 	evol= EVOL_grout.values[i].data

		# 	a = (S_grout.values[i].data[0])*evol
		# 	elemId=S_grout.values[i].elementLabel
		# 	myStress_data.setdefault(elemId,[]).append(a)
