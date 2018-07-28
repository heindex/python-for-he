class Students:
	role = 'name,age'
	def __init__(self,nm,ag,gd=[]):
		self.name = nm
		self.age = ag
		self.grade = gd
	def get_name(self):
		print(str(self.name))
	def get_age(self):
		print(int(self.age))
	def get_course(self):
		print(int(max(self.grade)))
zm = Students('zhangming',20,[69,88,100])
hzc = Students('hezhichao',21,[100,100,100])
zm.get_name()
zm.get_age()
zm.get_course()
hzc.get_name()
hzc.get_age()
hzc.get_course()
