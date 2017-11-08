from visualization import *
import matplotlib.pyplot as plt
import numpy as np
import csv

filenames = ['30lc']
for filname in filenames:	
	odb = openOdb(path=str(filname)+'.odb');
	
	myAssembly = odb.rootAssembly;
	instances=odb.rootAssembly.instances['PART-1-1']
	
	numframes = odb.steps['Step-1'].frames;
	numframesM = odb.steps['Step-1'].frames[-1];
	fStress=[];
	frameEVOL=[];
	frameSTRAIN=[];
	frameSTRAINSE=[];
	#Get only the last frame [-1]
	list_h = []
	list_d = []
	SL=[]
	Setname=['HARD']

	for s in Setname:
		Stressy=[];
		Strainy=[];
		Sets=odb.rootAssembly.instances['PART-1-1'].elementSets[str(s)]
		stressM=numframesM.fieldOutputs['S']
		StressL=stressM.getSubset(region=Sets,position=INTEGRATION_POINT)

		for i in range(0,len(numframes)):
			fStress.insert(0,numframes[i].fieldOutputs['S'].getSubset(region=Sets,position=INTEGRATION_POINT));
			# frameEVOL.insert(0,numframes[i].fieldOutputs['EVOL'].getSubset(region=Sets,elementType='C3D4'));
			frameSTRAIN.insert(0,numframes[i].fieldOutputs['LE'].getSubset(region=Sets,position=INTEGRATION_POINT));
			frameEVOL.insert(0,numframes[i].fieldOutputs['IVOL'].getSubset(region=Sets,elementType='C3D10'));
			frameSTRAINSE.insert(0,numframes[i].fieldOutputs['SENER'].getSubset(region=Sets,position=INTEGRATION_POINT));
			Tot_Vol=0;
			
			Tot_Stress=0;
			Tot_Strain=0;
			Tot_StressSE=0;
			Tot_StrainSE=0;
			Tot_StressSE=[];
			Tot_StrainSE=[];
			for j in range(0,len(fStress[-1].values)):
			    Tot_Vol=Tot_Vol+frameEVOL[0].values[j].data;
			    Tot_Stress=Tot_Stress+fStress[0].values[j].data * frameEVOL[0].values[j].data;
			    Tot_Strain=Tot_Strain+frameSTRAIN[0].values[j].data* frameEVOL[0].values[j].data;
			    Tot_StressSE=fStress[0].values[j].data 
			    Tot_StrainSE=Tot_StrainSE+frameSTRAINSE[0].values[j].data* frameEVOL[0].values[j].data;


			Avg_Stress = Tot_Stress/Tot_Vol
			Avg_Strain = Tot_Strain/Tot_Vol

			Avg_StrainEner = Tot_StrainSE/Tot_Vol

			S11 = Avg_Stress[0]
			S22 = Avg_Stress[1]
			S33 = Avg_Stress[2]
			L11 = Avg_Strain[0]
			L22 = Avg_Strain[1]
			L33 = Avg_Strain[2]
			Stressy.append(S22)
			Strainy.append(L22)
			SED = Avg_StrainEner


			for v in StressL.values:
				SL.append(v.data[1])


				L=np.sort(SL)[::-1]

				percent10= np.around(0.1*len(L))
				maxstress10percent=L[:percent10].mean()

				ars=[maxstress10percent]

	
		print str(s)
		print "Stress",Stressy
		print "StrainENER",Strainy
		# idx += 1
	with open('all.csv', 'a') as f:
		writer = csv.writer(f, delimiter='\t')
		writer.writerow(["Stress"+str(s),"Strain"+str(s)])
		writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
		writer.writerows(zip(Stressy,Strainy,SED,ars))
	headers.append(["Stress","Strain"])

# np.savetxt(str(filname)+'.csv',d)
		
# with open(str(filname)+'.csv', 'a') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(headers)
# 	writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
# 	writer.writerows(d)
	
