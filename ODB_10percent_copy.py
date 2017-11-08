from visualization import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from itertools import islice

filenames = ['50lc']
for filname in filenames:	
	odb = openOdb(path=str(filname)+'.odb');
	numframes = odb.steps['Step-1'].frames
	myAssembly = odb.rootAssembly;
	instances=odb.rootAssembly.instances['PART-1-1']
	
	# Sets=odb.rootAssembly.instances['PART-1-1'].elementSets['HARD']
	# SL=[]
	# StressL=stress.getSubset(region=Sets,position=INTEGRATION_POINT)
	# for v in StressL.values:
	# 	SL=append(v.data[1])
	SL=[]
	Setname=['HARD']
	for s in Setname:
		Stressy=[];
		Strainy=[];
		
		Sets=odb.rootAssembly.instances['PART-1-1'].elementSets[str(s)]
		Tot_Stress=[];
		print Tot_Stress

		for i in range(0,len(numframes)):
			fStress.insert(0,numframes[i].fieldOutputs['S'].getSubset(region=Sets,position=INTEGRATION_POINT));


			
			# for j in range(0,len(fStress)):
			# 	a=0;
			# 	a=fStress[0].values[j].data[1]

			# 	Tot_Stress.append(a)



			for v in Tot_Stress:
				Tot_Stress.append(v.data[1])
				L=np.sort(SL)[::-1]
				percent10= np.around(0.1*len(L))
				maxstress10percent=L[:percent10].mean()

				ars=[maxstress10percent]


		# sorted(SL, key=float, reverse=True)
		# with open(str(filname)+'.csv', 'a') as f:
		# 	writer = csv.writer(f, delimiter='\t')
		# 	writer.writerow(["MAXStress"+str(s)])
		# 	writer = csv.writer(f, delimiter='\t',lineterminator='\n',)
		# # 	writelines(str(maxstress10percent)+'\n')
			
		# # np.savetxt(str(filname)+'.csv', ars, delimiter=',', fmt='%s',header=str(s))
		# dir= ("D:\SIMULIA\Temp")
		# f1=file(dir+os.sep+str(filname)+'.csv','a')
		# f1.writelines("StressMAX10_"+str(s)+"_"+str(filname)+'\n')
		# f1.writelines(str(maxstress10percent)+'\n')
		# f1.close()
 
