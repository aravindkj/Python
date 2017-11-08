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



#Get all nodes
nodesAll=mdb.models['Model-1'].rootAssembly.sets['local'].nodes
nodesAllCoor=[]
for nod in mdb.models['Model-1'].rootAssembly.sets['Part-1'].nodes:
        nodesAllCoor.append(nod.coordinates)
repConst=0