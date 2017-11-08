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



# ['TOP','BOTTOM','BOTTOMLEFT','BOTTOMRIGHT','TOPLEFT','TOPRIGHT']
INTREST = ['TOP','BOTTOM','LEFT','RIGHT']
for nod in INTREST:
	for i in range(0,1000):
		mdb.models['Model-1'].boundaryConditions((str(nod)+'-'+str(i))
