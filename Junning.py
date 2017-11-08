>>> from part import *
>>> from material import *
>>> from section import *
>>> from assembly import *
>>> from step import *
>>> from interaction import *
>>> from load import *
>>> from mesh import *
>>> from optimization import *
>>> from job import *
>>> from sketch import *
>>> from visualization import *
>>> from connectorBehavior import *
>>> myODB = openOdb('tt.odb')
>>> step = myODB.steps['Step-1']
>>> frame = step.frames[-1]
>>> f = frame.fieldOutputs
>>> print f
{'COORD': 'FieldOutput object', 'E': 'FieldOutput object', 'S': 'FieldOutput object', 'U': 'FieldOutput object'}
>>> dd = frame.fieldOutputs['U']
>>> cc = frame.fieldOutputs['COORD']
>>> set = myODB.rootAssembly
>>> print set
({'connectorOrientations': 'ConnectorOrientationArray object', 'datumCsyses': 'Repository object', 'elementSets': 'Repository object', 'elements': 'OdbMeshElementArray object', 'instances': 'Repository object', 'name': 'ASSEMBLY', 'nodeSets': 'Repository object', 'nodes': 'OdbMeshNodeArray object', 'pretensionSections': 'OdbPretensionSectionArray object', 'rigidBodies': 'OdbRigidBodyArray object', 'sectionAssignments': 'SectionAssignmentArray object', 'surfaces': 'Repository object'})
>>> set = set.nodeSets
>>> print set
{' ALL NODES': 'OdbSet object', 'SET-1': 'OdbSet object', 'SET-2': 'OdbSet object'}
>>> set = myODB.rootAssembly.instances['PART-1-1']
>>> print set
({'analyticSurface': None, 'beamOrientations': 'BeamOrientationArray object', 'elementSets': 'Repository object', 'elements': 'OdbMeshElementArray object', 'embeddedSpace': THREE_D, 'materialOrientations': 'MaterialOrientationArray object', 'name': 'PART-1-1', 'nodeSets': 'Repository object', 'nodes': 'OdbMeshNodeArray object', 'rebarOrientations': 'RebarOrientationArray object', 'rigidBodies': 'OdbRigidBodyArray object', 'sectionAssignments': 'SectionAssignmentArray object', 'surfaces': 'Repository object', 'type': DEFORMABLE_BODY})
>>> set = set.nodeSets
>>> print set
{'SET-1': 'OdbSet object', 'SET-2': 'OdbSet object'}
>>> set = set['Set-2']
KeyError: Set-2
>>> set = set['SET-2']
>>> len(set)
TypeError: object of type 'OdbSet' has no len()
>>> print set
({'elements': None, 'faces': None, 'instanceNames': None, 'instances': None, 'isInternal': False, 'name': 'SET-2', 'nodes': 'OdbMeshNodeArray object'})
>>> len(set.nodes)
44
>>> dd
openOdb(r'D:/SIMULIA/Temp/tt.odb').steps['Step-1'].frames[1].fieldOutputs['U']
>>> dd1 = dd.getSubset(region=set)
>>> len(dd1.values)
44