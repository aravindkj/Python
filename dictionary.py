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

part = ['Hard','Soft']

for i in part:
    dict = mdb.models['Model-1'].parts

    A=dict.keys()

    number = [s for s in A if str(i) in s]

    length= len(number)
    for n in range(1,length+1):
        mdb.models['Model-1'].parts[str(i)+'-'+str(n)].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=21)
        mdb.models['Model-1'].parts[str(i)+'-'+str(n)].setMeshControls(elemShape=TET, regions=
            mdb.models['Model-1'].parts[str(i)+'-'+str(n)].cells, technique=FREE)
        mdb.models['Model-1'].parts[str(i)+'-'+str(n)].setElementType(elemTypes=(ElemType(
            elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
            elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
            regions=(mdb.models['Model-1'].parts[str(i)+'-'+str(n)].cells, ))
        mdb.models['Model-1'].parts[str(i)+'-'+str(n)].generateMesh()




            for j in range(1,5):
                a = mdb.models['Model-1'].rootAssembly
                a.DatumCsysByDefault(CARTESIAN)
                p = mdb.models['Model-1'].parts[str(i)+'-'+str(n)+'-mesh-'+str(j)]
                a.Instance(name=str(i)+'-'+str(n)+'-mesh-'+str(j), part=p, dependent=ON)
















# part = ['Joint']
# Hard=35000
# Hardpr=0.3
# Soft=25000
# Softpr=0.3
# Interspoke=25000
# Interspokepr=0.3
# Joint=1500
# Jointpr=0.3



# for i in part: 
#     for n in range(1,5000):
        # mdb.models['Model-1'].Material(name='Hard')
        # mdb.models['Model-1'].materials['Hard'].Elastic(table=((Hard, Hardpr), ))
        # mdb.models['Model-1'].HomogeneousSolidSection(material='Hard', name= 'Hard', thickness=None)

        # mdb.models['Model-1'].Material(name='Soft')
        # mdb.models['Model-1'].materials['Soft'].Elastic(table=((Soft, Softpr), ))
        # mdb.models['Model-1'].HomogeneousSolidSection(material='Soft', name= 'Soft', thickness=None)

        # mdb.models['Model-1'].Material(name='Interspoke')
        # mdb.models['Model-1'].materials['Interspoke'].Elastic(table=((Interspoke, Interspokepr), ))
        # mdb.models['Model-1'].HomogeneousSolidSection(material='Interspoke', name= 'Interspoke', thickness=None)

        # mdb.models['Model-1'].Material(name='Joint')
        # mdb.models['Model-1'].materials['Joint'].Elastic(table=((Joint, Jointpr), ))
        # mdb.models['Model-1'].HomogeneousSolidSection(material='Joint', name= 'Joint', thickness=None)


        # mdb.models['Model-1'].materials['Joint'].Hyperelastic(materialType=ISOTROPIC, 
        #     testData=OFF, type=OGDEN, n=3, volumetricResponse=VOLUMETRIC_DATA, table=((
        #     0.0326, 8.41, 0.000788, 25.0, 0.00103, -18.94, 12.47, 0.0, 0.0), ))

    ##### mdb.models['Model-1'].materials['Joint'].elastic.setValues(
    ###     type=ENGINEERING_CONSTANTS, table=((30.0, 30.0, 300.0, 0.45, 0.045, 0.045, 
    ####     10.3448, 20.0, 20.0), ))

        # p = mdb.models['Model-1'].parts[str(i)+'-'+str(n)]
        # c = p.cells
        # cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
        # region = p.Set(cells=cells, name=str(i)+'-'+str(n))
        # p = mdb.models['Model-1'].parts[str(i)+'-'+str(n)]
        # p.SectionAssignment(region=region, sectionName=str(i), offset=0.0, 
        #     offsetType=MIDDLE_SURFACE, offsetField='', 
        #     thicknessAssignment=FROM_SECTION)






# for i in part: 
# #     for n in range(1,5000):
#         mdb.models['Model-1'].parts[str(i)+'-'+str(n)].seedPart(deviationFactor=0.1, 
#         minSizeFactor=0.1, size=21)
#         mdb.models['Model-1'].parts[str(i)+'-'+str(n)].setMeshControls(elemShape=TET, regions=
#             mdb.models['Model-1'].parts[str(i)+'-'+str(n)].cells, technique=FREE)
#         mdb.models['Model-1'].parts[str(i)+'-'+str(n)].setElementType(elemTypes=(ElemType(
#             elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
#             elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
#             regions=(mdb.models['Model-1'].parts[str(i)+'-'+str(n)].cells, ))
#         mdb.models['Model-1'].parts[str(i)+'-'+str(n)].generateMesh()
    
#         mdb.models['Model-1'].parts[str(i)+'-'+str(n)].PartFromMesh(copySets=True, name=
#             str(i)+'-'+str(n)+'-mesh-1')
#         mdb.models['Model-1'].Part(compressFeatureList=ON, mirrorPlane=XZPLANE, name=
#             str(i)+'-'+str(n)+'-mesh-2', objectToCopy=
#             mdb.models['Model-1'].parts[str(i)+'-'+str(n)+'-mesh-1'])
#         mdb.models['Model-1'].Part(compressFeatureList=ON, mirrorPlane=YZPLANE, name=
#             str(i)+'-'+str(n)+'-mesh-3', objectToCopy=
#             mdb.models['Model-1'].parts[str(i)+'-'+str(n)+'-mesh-2'])
#         mdb.models['Model-1'].Part(compressFeatureList=ON, mirrorPlane=XZPLANE, name=
#            str(i)+'-'+str(n)+'-mesh-4', objectToCopy=
#             mdb.models['Model-1'].parts[str(i)+'-'+str(n)+'-mesh-3']) 

# #lists
# temp = []
# dictList = []
# for key, value in dict.iteritems(mdb.models['Model-1'].parts):
#     aKey = key
#     aValue = value
#     temp.append(aKey)
#     temp.append(aValue)
#     dictList.append(temp) 
#     aKey = ""
#     aValue = ""