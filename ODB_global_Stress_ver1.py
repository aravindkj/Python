from visualization import *
import matplotlib.pyplot as plt
import numpy as np
import csv

filenames = ['Compression_global_base']
for filname in filenames:	
	odb = openOdb(path=str(filname)+'.odb');
	
	myAssembly = odb.rootAssembly;
	instances=odb.rootAssembly.instances['PART-1-1']
	
	numframes = odb.steps['Step-1'].frames;
	fStress=[];
	frameIVOL=[];
	frameSTRAIN=[];
	#Get only the last frame [-1]
	list_h = []
	list_d = []
	Setname=['SET-1']
	# d = np.zeros((np.size(Setname)*2,len(numframes)))
	# print np.shape(d)
	# idx = 0
	# headers = []
	for s in Setname:
		Stressy=[];
		Strainy=[];
		Sets=odb.rootAssembly.instances['PART-1-1'].elementSets[str(s)]
		for i in range(0,len(numframes)):
			fStress.insert(0,numframes[i].fieldOutputs['S'].getSubset(region=Sets,position=INTEGRATION_POINT));
			frameIVOL.insert(0,numframes[i].fieldOutputs['IVOL'].getSubset(region=Sets,elementType='C3D4'));
			frameSTRAIN.insert(0,numframes[i].fieldOutputs['LE'].getSubset(region=Sets,position=INTEGRATION_POINT));


			#Total Volume
			Tot_Vol=0;
			
			Tot_Stress=0;
			Tot_Strain=0;
			for j in range(0,len(fStress[-1].values)):
			    Tot_Vol=Tot_Vol+frameIVOL[0].values[j].data;
			    Tot_Stress=Tot_Stress+fStress[0].values[j].data * frameIVOL[0].values[j].data;
			    Tot_Strain=Tot_Strain+frameSTRAIN[0].values[j].data* frameIVOL[0].values[j].data;

			#Calculate Average
			Avg_Stress = Tot_Stress/Tot_Vol
			Avg_Strain = Tot_Strain/Tot_Vol

			S11 = Avg_Stress[0]
			S22 = Avg_Stress[1]
			S33 = Avg_Stress[2]
			L11 = Avg_Strain[0]
			L22 = Avg_Strain[1]
			L33 = Avg_Strain[2]
			

			Stressy.append(S22)
			Strainy.append(L22)

			# d[idx,i] = S22
			# d[idx+1,i] =L22

		print str(s)
		print "Stress",Stressy
		print "StrainENER",Strainy

		print str(s)
		print "Stress",Stressy
		print "StrainENER",Strainy
		with open(str(filname)+'.csv', 'a') as f:
			writer = csv.writer(f, delimiter='\t')
			writer.writerow(["Stress"+str(s),"Strain"+str(s)])
			writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
			writer.writerows(zip(Stressy,Strainy))





	
