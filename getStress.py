RVE_para={}
stif=zeros([6,6])
RVE_para["mesh"]=0.05
RVE_para["length"]=1.0000
RVE_para["volumeFraction"]=0.47
RVE_para["elementCode"]=C3D20
RVE_para["matrixProperties"]=(68.3,0.3)
RVE_para["fiberProperties"]=(379.3,0.1)
RVE_para["strain"]=0.0001
RVE_para["prestrain"]=[0.0000,0.0000,0.0000,0.0000,0.0000,0.0000]
for n in range(len(RVE_para["prestrain"])):
	RVE_para["prestrain"]=[0.0000,0.0000,0.0000,0.0000,0.0000,0.0000]
	RVE_para["number"]=n
	RVE_para["name"]='RVE'+str(n+1)
	RVEModel = mdb.Model(RVE_para["name"])
if (n<6):
	RVE_para["prestrain"][n]=RVE_para["strain"]
else:
	RVE_para["prestrain"]=[RVE_para["strain"],RVE_para["strain"],RVE_para["strain"],
0.0000,0.0000,0.0000]
k=8-n
RVE_para["prestrain"][k]=0.0000
RVEPart=CreatePart(RVE_para,RVEModel)
CreateMaterial(RVE_para,RVEModel)
CreateSection(RVE_para,RVEModel,RVEPart)
RVEAssembly=CreateAssembly (RVE_para,RVEModel,RVEPart)
CreateStep (RVE_para,RVEModel )
CreateBoudary (RVE_para,RVEModel,RVEPart,RVEAssembly)
CreateLoad (RVE_para,RVEModel,RVEAssembly)
CreateJob (RVE_para)
if (n<6):
	stif[n][n]=CreateResult(RVE_para,stif)
if (5<n<8):
	stif[0][n-5]=CreateResult(RVE_para,stif)
	stif[n-5][0]=CreateResult(RVE_para,stif)
if (n==8):
	stif[n-7][n-6]=CreateResult(RVE_para,stif)
	stif[n-6][n-7]=CreateResult(RVE_para,stif)
print stif
stif1=mat(stif)
print stif1
compliance=stif1**(-1)
print "compliance matrix",print compliance