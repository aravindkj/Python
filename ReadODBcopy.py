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


names=['hyperelastic_test'] 
nodeNumber=1
#Name of the step of interest. By default it is Step-1
nameOfStep='Step-1'

for y in range(len(names)):
	NameOfFile=names[y]+'.csv'
	
	FileResultsX=open(NameOfFile,'wb')

	Name=names[y]+'.odb'
	myOdb = openOdb('hyperelastic_test_timeframes.odb')
	lastStep=myOdb.steps[nameOfStep]		
	for z in range(len(lastStep.frames)):
		lastFrame = myOdb.steps[nameOfStep].frames[z]
		Times=lastFrame.frameValue
		#RF is where the reaction forces are saved. Use U for displacements etc.
		ReactionForce = lastFrame.fieldOutputs['U']

		for v in ReactionForce.values:
			if v.nodeLabel == nodeNumber:
				FileResultsX.write('%10.8E\t' % (v.data[0]))
				# FileResultsX.write('%10.8E\t %10.8E\t\n' % (v.data[1],Times))
				# Comment the last line and uncomment the two following lines for 3D models
				FileResultsX.write('%10.8E\t' % (v.data[1]))
				FileResultsX.write('%10.8E\t %10.8E\t\n' % (v.data[2],Times))

	FileResultsX.write('\n')

	myOdb.close()	
	FileResultsX.close()