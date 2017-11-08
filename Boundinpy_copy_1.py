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




# part=['Part-1']
# for n in part:
# #     for n in range(1,25):
# #         a.Instance(name=str(i)+'-'+str(n)+'-'+str(n), part=p, dependent=ON)
# #         a.InstanceFromBooleanMerge(name='Hard', instances=(str(i)+'-'+str(n)+'-'+str(n) ), 
# #                 originalInstances=SUPPRESS, domain=GEOMETRY)




# Hard=35000
# Hardpr=0.3
# Soft=25000
# Softpr=0.3
# Interspoke=25000
# Interspokepr=0.3


# mdb.models['Model-1'].Material(name='Hard')
# mdb.models['Model-1'].materials['Hard'].Elastic(table=((Hard, Hardpr), ))
# mdb.models['Model-1'].HomogeneousSolidSection(material='Hard', name= 'Hard', thickness=None)

# mdb.models['Model-1'].Material(name='Soft')
# mdb.models['Model-1'].materials['Soft'].Elastic(table=((Soft, Softpr), ))
# mdb.models['Model-1'].HomogeneousSolidSection(material='Soft', name= 'Soft', thickness=None)

# mdb.models['Model-1'].Material(name='Interspoke')
# mdb.models['Model-1'].materials['Interspoke'].Elastic(table=((Interspoke, Interspokepr), ))
# mdb.models['Model-1'].HomogeneousSolidSection(material='Interspoke', name= 'Interspoke', thickness=None)

# mdb.models['Model-1'].Material(name='Interspoke')
# mdb.models['Model-1'].materials['Interspoke'].Elastic(table=((Interspoke, Interspokepr), ))
# mdb.models['Model-1'].HomogeneousSolidSection(material='Interspoke', name= 'Perichondrium', thickness=None)

# mdb.models['Model-1'].Material(name='Joint')
# mdb.models['Model-1'].materials['Joint'].Hyperelastic(materialType=ISOTROPIC, 
#     testData=OFF, type=OGDEN, n=3, volumetricResponse=VOLUMETRIC_DATA, table=((
#     0.0326, 8.41, 0.000788, 25.0, 0.00103, -18.94, 12.47, 0.0, 0.0), ))
# mdb.models['Model-1'].HomogeneousSolidSection(material='Joint', name= 'Joint', thickness=None)
# a = mdb.models['Model-1'].rootAssembly
# part = ['Part-1']
# h=[]
# for i in part:
# 	dict = mdb.models['Model-1'].parts

# 	A=dict.keys()

# 	number = [s for s in A if str(i) in s]
# 	print number
# 	length= len(number)
# 	print length
# 	for index,n in enumerate(number):
# 		print n
# 		p = mdb.models['Model-1'].parts[str(n)]
# 		c = p.cells
# 		n1=p.nodes
# 		cells = c.getByBoundingBox(xMin=0,yMin=0,xMax=1000,yMax=1000)
		
# 		region = p.Set(cells=cells, name=str(n))
		

# 		# p.SectionAssignment(region=region, sectionName=str(i), offset=0.0, 
# 		#     offsetType=MIDDLE_SURFACE, offsetField='', 
# 		#     thicknessAssignment=FROM_SECTION)
		

# 		# print str(n)+'section'


# 		mdb.models['Model-1'].parts[str(n)].seedPart(deviationFactor=0.1, 
# 		    minSizeFactor=0.1, size=16)
# 		mdb.models['Model-1'].parts[str(n)].setMeshControls(elemShape=TET, regions=
# 		    mdb.models['Model-1'].parts[str(n)].cells, technique=FREE)
# 		mdb.models['Model-1'].parts[str(n)].setElementType(elemTypes=(ElemType(
# 		    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
# 		    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
# 		    regions=(mdb.models['Model-1'].parts[str(n)].cells, ))
# 		mdb.models['Model-1'].parts[str(n)].generateMesh()
# 		print str(n)+'-mesh'
		
		
		
		

# 		# p.PartFromMesh(copySets=True, name=str(n)+'-mesh')
# 		# a = mdb.models['Model-1'].rootAssembly
# 		# a.DatumCsysByDefault(CARTESIAN)
# 		# x = mdb.models['Model-1'].parts[str(n)+'-mesh']
# 		# a.Instance(name=str(n)+'-mesh', part=x, dependent=ON)
		
# 		# h=[]
# 		# a1 = mdb.models['Model-1'].rootAssembly
# 		# # n1 = a1.instances[str(n)+'-mesh']
# 		# name = a1.nodes.getByBoundingBox(xMin=0,yMin=0,xMax=1000,yMax=1000)
# 		# h.append(name)
# 		# a1.Set(nodes=name, name='PerBound')

		
		




        # mdb.models['Model-1'].parts[str(n)].PartFromMesh(copySets=True, name=
        #     str(n)+'-mesh-1')
        # mdb.models['Model-1'].Part(compressFeatureList=ON, mirrorPlane=XZPLANE, name=
        #     str(n)+'-mesh-2', objectToCopy=
        #     mdb.models['Model-1'].parts[str(n)+'-mesh-1'])
        # mdb.models['Model-1'].Part(compressFeatureList=ON, mirrorPlane=YZPLANE, name=
        #     str(n)+'-mesh-3', objectToCopy=
        #     mdb.models['Model-1'].parts[str(n)+'-mesh-2'])
        # mdb.models['Model-1'].Part(compressFeatureList=ON, mirrorPlane=XZPLANE, name=
        #    str(n)+'-mesh-4', objectToCopy=
        #     mdb.models['Model-1'].parts[str(n)+'-mesh-3']) 

# l=753
# w=350


# p = mdb.models['Model-1'].rootAssembly
# n = p.instances['Part-2-1'].nodes
# # # print n
# h=[]
# a=0.01
# top = n.getByBoundingBox(xMin=0+a,yMin=w-a,xMax=l+a,yMax=w+a)
# bottom = n.getByBoundingBox(xMin=0-a,yMin=0-a,xMax=l+a,yMax=0+a)
# left = n.getByBoundingBox(xMin=0-a,yMin=0-a,xMax=0+a,yMax=w+a)
# right = n.getByBoundingBox(xMin=l-a,yMin=0-a,xMax=l+a,yMax=w+a)
# h.append(top)
# h.append(bottom)
# h.append(left)
# h.append(right)
# p.Set(nodes=h, name='PerBound')

# # right2 = n.getByBoundingBox(xMin=450.333206,yMin=0-a,xMax=0,yMax=866.025E-03)
# # h.append(right2)
# # p.Set(nodes=h, name='plane')


(CoorFixNode,NameRef1, NameRef2,NameRef3)=PeriodicBound3D(mdb,'Model-1','PerBound',[(434.744751, 0., 0),( 0,753, 0),(0., 0., -350)],)

# # ###############################################################################
# # ####CREATE STEP AND APPLY BC
# # ##############################################################################
# # mdb.models['Model-1'].StaticStep(name='Step-1', nlgeom=ON, previous='Initial')
# # #Apply boundary conditions on reference nodes
# # DefMat=[(17.33,0.0,0.0),(0.0,UNSET,0.0), (0.0,0.0,0.0)]
# # mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
# #     distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
# #     'BC-REF-1', region=Region(referencePoints=(
# #     mdb.models['Model-1'].rootAssembly.instances[NameRef1].referencePoints[1], 
# #     )), u1=DefMat[0][0], u2=DefMat[0][1], u3=DefMat[0][2], ur1=UNSET,ur2=UNSET,ur3=UNSET)






# # mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
# #     distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
# #     'BC-REF-2', region=Region(referencePoints=(
# #     mdb.models['Model-1'].rootAssembly.instances[NameRef2].referencePoints[1], 
# #     )), u1=DefMat[1][0], u2=DefMat[1][1], u3=DefMat[1][2], ur1=UNSET,ur2=UNSET,ur3=UNSET)
# # mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
# #     distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
# #     'BC-REF-3', region=Region(referencePoints=(
# #     mdb.models['Model-1'].rootAssembly.instances[NameRef3].referencePoints[1], 
# #     )), u1=DefMat[2][0], u2=DefMat[2][1], u3=DefMat[2][2], ur1=UNSET,ur2=UNSET,ur3=UNSET)
# # mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
# #     distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
# #     'BC-FIXNODE', region=Region(
# #     nodes=mdb.models['Model-1'].rootAssembly.instances['Part-7-1'].nodes.getByBoundingSphere(center=CoorFixNode, radius=0.001)), u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET,ur3=UNSET)

# # # # mdb.save()