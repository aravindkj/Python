from visualization import *
import matplotlib.pyplot as plt
import numpy as np
import csv

filenames = ['TILE5000']
for filname in filenames:	
	odb = openOdb(path=str(filname)+'.odb');
	
	myAssembly = odb.rootAssembly;
	instances=odb.rootAssembly.instances['PART-1-1']
	
	numframes = odb.steps['Step-1'].frames;
	fStress=[];
	#Get only the last frame [-1]

	Setname=['ELEM']

	for s in Setname:
		Stressy=[];
		Strainy=[];
		Sets=odb.rootAssembly.instances['PART-1-1'].elementSets[str(s)]
		for i in range(0,len(numframes)):
			fStress.insert(0,numframes[i].fieldOutputs['S'].getSubset(region=Sets,position=INTEGRATION_POINT));
			print len(fStress)

			#Total Volume
		# 	Tot_Vol=0;
			
		# 	Tot_Stress=0;
		# 	Tot_Strain=0;
			for j in range(0,len(fStress[-1].values)):
		# 	    Tot_Vol=Tot_Vol+frameEVOL[0].values[j].data;
			    Tot_Stress=fStress[0].values[j].data;
		# 	    Tot_Strain=Tot_Strain+frameSTRAIN[0].values[j].data;

		# 	#Calculate Average
		# 	Avg_Stress = np.mean(Tot_Stress);
		# 	Avg_Strain = np.mean(Tot_Strain);

		# 	# S11 = Avg_Stress[0]
		# 	# S22 = Avg_Stress[1]
		# 	# S33 = Avg_Stress[2]
		# 	# L11 = Avg_Strain[0]
		# 	# L22 = Avg_Strain[1]
		# 	# L33 = Avg_Strain[2]
			

		# 	Stressy.append(Avg_Stress)
		# 	Strainy.append(Avg_Strain)

		# 	# d[idx,i] = S22
		# 	# d[idx+1,i] =L22

		# print str(s)
		# print "Stress",np.mean(Avg_Stress)
		# print "Strain",np.mean(Avg_Strain)
		# # idx += 1
		# with open(str(filname)+'.csv', 'a') as f:
		# 	writer = csv.writer(f, delimiter='\t')
		# 	writer.writerow(["Stress"+str(s),"Strain"+str(s)])
		# 	writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
		# 	writer.writerows(zip(Stressy,Strainy))
# 		headers.append(["Stress"+str(s),"Strain"+str(s)])

# np.savetxt(str(filname)+'.csv',d)
		
# with open(str(filname)+'.csv', 'a') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(headers)
# 	writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
# 	writer.writerows(d)
	
