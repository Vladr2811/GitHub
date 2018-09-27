class Robot:

	totalRobots = 0
	totalRobotsWorking = 0
	RobotsArray = []

	def __init__(self,name,work):
		self.name = name
		self.work = work
		self.working = False
		Robot.RobotsArray.append(self)
		Robot.totalRobots += 1


	def destroy(self):
		print("{} has ben destroyed!".format(self.name))
		Robot.totalRobots -= 1
		if(self.working == True):
			Robot.totalRobotsWorking -= 1
			self.working = False
			Robot.printTotalRobots()

	def startWork(self):	
		print(("{} ready and started {}ing!").format(self.name,self.work.lower()))
		Robot.totalRobotsWorking += 1
		self.working = True
		Robot.printTotalRobots()


	def stopWork(self):
		print("{} ready and waiting for orders!".format(self.name))
		Robot.totalRobotsWorking -= 1
		self.working = False
		Robot.printTotalRobots()

	def getName(self):
		return self.name
	def setName(self,name):
		self.name = name
	def getWork(self):
		return self.work
	def setWork(self,work):
		self.work = work

	@classmethod
	def printTotalRobots(cls):
		print("There are {:d} robots avaliable and {:d} working".format((cls.totalRobots - cls.totalRobotsWorking), cls.totalRobotsWorking))
	
	@classmethod
	def getRobotsArray(cls):
		return cls.RobotsArray;
	


class NanoBot(Robot):

	def __init__(self,name,work,height,width):
		Robot.__init__(self,name,work)
		self.height = height
		self.width = width

	def canPass(self,height,width):
		if(self.height < height and self.width < width):
			print("Yes, I can pass!")

		else:
			print("Noooo, I can't pass :(")

	def getHeight(self):
		return self.height
	def setHeight(self,height):
		self.height = height
	def getWidth(self):
		return self.width
	def setWidth(self,width):
		self.width = width
	def botsToPass(array,height,width):
		returnArray = []
		for robot in array:
			if(isinstance(robot,NanoBot)):
				if(robot.getHeight() < height and robot.getWidth() < width):
					returnArray.append(robot)
		return returnArray


	



