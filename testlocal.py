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

###Create loops to go through all your global sets, and then the local sets too###
###Create loops to go through all your global sets, and then the local sets too### 
###Create loops to go through all your global sets, and then the local sets too### 
sets=['TOP','TOPL','TOLR','BOTTOM','BOTTOML','BOTTOMR']
for interest in sets:
	gDispSet = []
	gCoordSet = []

	###Reading the Global Coordinates and Displacments
	gOdb = openOdb(path = 'global-2-PBC.odb')
	gSet = gOdb.rootAssembly.nodeSets[str(interest)]
	gStep = gOdb.steps['Step-1']
	gFrame = gStep.frames[-1]
	gCoord = gFrame.fieldOutputs['COORD'].getSubset(region=gSet).values
	gDisp = gFrame.fieldOutputs['U'].getSubset(region=gSet).values

	for i in range(len(gCoord)):
		gCoordSet.append(np.array(gCoord[i].data))
		gDispSet.append(np.array(gDisp[i].data))

	#%%%%%Please add your exporting function (writing to txt file) here,  %%%%#
	#%%%%%so you can keep a track of what nodes you were using from global%%%%#
		
	#########################################################################################
	lDispSet = []
	lCoordSet = []
		
	###Create the Target Set for the Local Model
	m = mdb.models['Model-1']
	a = m.rootAssembly
	lSet = a.sets[str(interest)].nodes

	###Calculate the distances from target node to the four global nodes
	for i in range(len(lSet)):
		#print ('Processing Node-'+str(lSet[i].label)+' in the local model...')
		
		#Read the target node coordinates
		nCoord = np.array(lSet[i].coordinates)
		lCoordSet.append(nCoord)
		
		#Looping through all known global nodes to calculate distances
		distSet = []
		for j in range(len(gCoordSet)):
			distSet.append(np.linalg.norm(np.array(gCoordSet[j])-np.array(nCoord)))
		distSet = np.array(distSet)
		
		#Find the top four (minimum) distances and their indeces
		neighbourIndex = distSet.argsort()[:5][::1]
		
		#Save all neighbour coordinates and displacements into two arrays
		neighbourCoord = []
		neighbourDisp = []
		neighbourDist = []
		distSum = 0
		for j in range(5):
			neighbourCoord.append(gCoordSet[neighbourIndex[j]])
			neighbourDisp.append(gDispSet[neighbourIndex[j]])
			neighbourDist.append(distSet[neighbourIndex[j]])
			distSum = distSum + distSet[neighbourIndex[j]]
			print "distsum"
			print distsum
		#Calculating the linearly weighted displacements for this node
		lDispX = 0
		lDispY = 0
		lDispZ = 0
		for j in range(5):
			#Please feel free to distable #print function. I used them for de-bugging#
			#print (str(np.sum(neighbourDist[0:j+1])/distSum*100)+ '% done!')
			lDispX = lDispX + neighbourDist[-j-1]/distSum*neighbourDisp[j][0]
			#print ('Neighbour ' + str(j+1) + 'DipsX is ' + str(neighbourDisp[j][0]))
			lDispY = lDispY + neighbourDist[-j-1]/distSum*neighbourDisp[j][1]
			#print ('Neighbour ' + str(j+1) + 'DipsY is ' + str(neighbourDisp[j][1]))
			lDispZ = lDispZ + neighbourDist[-j-1]/distSum*neighbourDisp[j][2]
			#print ('Neighbour ' + str(j+1) + 'DipsZ is ' + str(neighbourDisp[j][2]))
		#print ('Displacments for this node are' + str(lDispX) + ' ' + str(lDispY) + ' ' + str(lDispZ))
		lDispSet.append(np.array([lDispX,lDispY,lDispZ]))
		
		#Assign the boundary condition to the node
		nodes1 = a.instances['Part-2-1'].nodes[lSet[i].label-1:lSet[i].label]
			#Change the instance name to fit your model
			#Same to other names in models, parts, and sets
		a.Set(nodes=nodes1, name='Node-'+str(lSet[i].label))
		region = a.sets['Node-'+str(lSet[i].label)]
		mdb.models['Model-1'].DisplacementBC(name='Node-'+str(lSet[i].label), createStepName='Step-1', 
		        region=region, u1=lDispX, u2=lDispY, u3=lDispZ, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
		        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
		        localCsys=None)
	#%%%%%Please add your exporting function (writing to txt file) here,  %%%%#
	#%%%%%so you can keep a track of what BCs you were assigning to local %%%%#		

	# mdb.save()

