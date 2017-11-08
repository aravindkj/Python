from visualization import *
import matplotlib.pyplot as plt
import numpy as np

filenames = ['TENSION_XY-Copy.odb']
for filname in filenames:	
	odb = openOdb(path=str(filname));
	
	myAssembly = odb.rootAssembly;
	instances=odb.rootAssembly.instances['PART-1-1']
	
	numframes = odb.steps['Step-1'].frames;
	fStress=[];
	frameEVOL=[];
	frameSTRAIN=[];
	#Get only the last frame [-1]
	Stressy=[];
	Strainy=[];
	for i in range(0,len(numframes)):
		fStress.insert(0,numframes[i].fieldOutputs['S'].getSubset(position=INTEGRATION_POINT));
		frameEVOL.insert(0,numframes[i].fieldOutputs['IVOL'].getSubset(position=INTEGRATION_POINT));
		frameSTRAIN.insert(0,numframes[i].fieldOutputs['LE'].getSubset(position=INTEGRATION_POINT));


		#Total Volume
		Tot_Vol=0;
		
		Tot_Stress=0;
		Tot_Strain=0;
		for j in range(0,len(fStress[-1].values)):
		    Tot_Vol=Tot_Vol+frameEVOL[0].values[j].data;
		    Tot_Stress=Tot_Stress+fStress[0].values[j].data * frameEVOL[0].values[j].data;
		    Tot_Strain=Tot_Strain+frameSTRAIN[0].values[j].data* frameEVOL[0].values[j].data;

		#Calculate Average
		Avg_Stress = Tot_Stress/Tot_Vol;
		Avg_Strain = Tot_Strain/Tot_Vol;

		S11 = Avg_Stress[0]
		S22 = Avg_Stress[1]
		S33 = Avg_Stress[2]
		L11 = Avg_Strain[0]
		L22 = Avg_Strain[1]
		L33 = Avg_Strain[2]
		

		Stressy.append(S22)
		Strainy.append(L22)
