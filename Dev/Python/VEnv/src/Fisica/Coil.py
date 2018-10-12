#Formulas y metodos acerca de bobinas
import numpy
import scipy
from scipy.misc import derivative
class Coil():
	#Atributes
	spiralNumber = 0
	surface = 0
	magCamp = 0
	gradesSec = 0
	#Constructor
	def __init__(self,spiralNumber,surface,magCamp=0,gradesSec=0):
		self.spiralNumber = spiralNumber
		self.surface = surface
		self.magCamp = magCamp
		self.gradesSec = gradesSec

	def getMagneticFlux(self,angleMCampSurface=None):
		if(angleMCampSurface != None):
			return self.spiralNumber * self.magCamp * self.surface * numpy.cos(angleMCampSurface * numpy.pi / 180)
		else:
			return self.spiralNumber * self.magCamp * self.surface 
	def getVolts(self):
		return self.getMagneticFlux()*(self.gradesSec*numpy.pi/180) * numpy.sin(self.gradesSec*numpy.pi/180)

bobina = Coil(150,numpy.pi*0.11**2,0.45,120)
print(bobina.gradesSec*numpy.pi/180)