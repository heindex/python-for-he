class Dictclass:
	def __init__(self,Dict):
		self.Dict = Dict
	def del_dict(self,dkey):
		self.Dict.pop(dkey)
		print(self.Dict)
	def get_dict(self,gkey):
		print(gkey if gkey in self.Dict else '未知')
	def get_key(self):
		l_key=[]
		for i in self.Dict:
			l_key.append(i)
		print(l_key)
	def update_dict(self,dictd):
		udict = self.Dict.copy()
		udict.update(dictd)
		l_values=[]
		for i in udict.keys():
			l_values.append(udict[i])
		print(l_values)	
di = Dictclass({'姓名':'何智超', '性别':'男', '年龄':'21','身价':'无穷'})
di.del_dict('身价')
di.get_dict('身价')
di.get_key()
di.update_dict({'生日':'1997.10.07', '籍贯':'河南'})

