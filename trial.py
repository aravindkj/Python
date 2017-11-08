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


from abaqus import *
from abaqusConstants import *
from odbAccess import *
import __main__

import numpy as np
import math
import sys
import timeit

eqStress, eqStrain = odb2ss('COMPRESSION_XY','PART-1-1','ALLELEMENTS')
np.savetxt(trialstressstrain, zip(eqStrain,eqStress))