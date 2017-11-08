from visualization import *
import matplotlib.pyplot as plt
import numpy as np
import csv

filenames = ['20lc']
for filname in filenames:	
	odb = openOdb(path=str(filname)+'.odb');
	
	myAssembly = odb.rootAssembly;
	instances=odb.rootAssembly.instances['PART-1-1']
	
	numframes = odb.steps['Step-1'].frames;
	fStress=[];
	frameIVOL=[];
	frameSTRAINSE=[];
	#Get only the last frame [-1]
	list_h = []
	list_d = []
	Setname=['HARD','SOFT']
	# d = np.zeros((np.size(Setname)*2,len(numframes)))
	# print np.shape(d)
	# idx = 0
	# headers = []

	for s in Setname:
		Stressy=[];
		Strainy=[];
		Tot_Vol=[];

		Tot_StressSE=[];
		Tot_StrainSE=[];
		Sets=odb.rootAssembly.instances['PART-1-1'].elementSets[str(s)]
		for i in range(0,len(numframes)):
			fStress.insert(0,numframes[i].fieldOutputs['S'].getSubset(region=Sets,position=INTEGRATION_POINT));
			frameIVOL.insert(0,numframes[i].fieldOutputs['IVOL'].getSubset(region=Sets,elementType='C3D10'));
			frameSTRAINSE.insert(0,numframes[i].fieldOutputs['SENER'].getSubset(region=Sets,position=INTEGRATION_POINT));

			for j in range(0,len(fStress[-1].values)):
			    Tot_Vol=Tot_Vol+frameIVOL[0].values[j].data;
			    Tot_StressSE=fStress[0].values[j].data 
			    Tot_StrainSE=Tot_StrainSE+frameSTRAINSE[0].values[j].data* frameIVOL[0].values[j].data;

			#Calculate Average
			# Avg_Stress = Tot_StressSE/Tot_Vol
			# Avg_Strain = Tot_StrainSE/Tot_Vol
			Avg_StrainEner = Tot_StrainSE/Tot_Vol


			# S11 = Avg_Stress[0]
			# S22 = Avg_Stress[1]
			# S33 = Avg_Stress[2]
			# L11 = Avg_Strain[0]
			# L22 = Avg_Strain[1]
			# L33 = Avg_Strain[2]
			SED = Avg_StrainEner
			

			# Stressy.append(S22)
			Strainy.append(SED)

			# d[idx,i] = S22
			# d[idx+1,i] =L22

		# print str(s)
		# print "Stress",Stressy
		# print "StrainENER",Strainy
		# # idx += 1
		dir= ("D:\SIMULIA\Temp")
		f1=file(dir+os.sep+'all.csv','a')
		f1.writelines("SED_"+str(s)+"_"+str(filname)+'\n')
		f1.writelines(str(SED)+'\n')
		f1.close()

os.system('python ODB_STRESS_STRAIN.py')


		
# with open(str(filname)+'.csv', 'a') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(headers)
# 	writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
# 	writer.writerows(d)
	
