from visualization import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from itertools import islice

filenames = ['30lc']
for filname in filenames:	
	odb = openOdb(path=str(filname)+'.odb');
	numframes = odb.steps['Step-1'].frames[-1]
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
		Sets=odb.rootAssembly.instances['PART-1-1'].elementSets[str(s)]
		
		stressM=numframes.fieldOutputs['S']
		StressL=stressM.getSubset(region=Sets,position=INTEGRATION_POINT)
		
		for v in StressL.values:
			SL.append(v.data[1])


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
			
		# np.savetxt(str(filname)+'.csv', ars, delimiter=',', fmt='%s',header=str(s))
		dir= ("D:\SIMULIA\Temp")
		f1=file(dir+os.sep+str(filname)+'.csv','a')
		f1.writelines("StressMAX10_"+str(s)+"_"+str(filname)+'\n')
		f1.writelines(str(maxstress10percent)+'\n')
		f1.close()
 
