class SIMS:
	def __init__(self,Dict):
		self.Dict = Dict
	def add_info(self,aDict):
		self.Dict.update(aDict)
		print(self.Dict)
	def del_info(self,dkey):
		self.Dict.pop(dkey)
		print(self.Dict)
	def mod_info(self,mkey,mval):	
		self.Dict[mkey]=mval
		print(self.Dict)
	def see_info(self,skey):
		print(skey,':',self.Dict[skey] if skey in self.Dict else '未知')
heindex = SIMS({'艺术':'300', '数学':'150', '语文':'150', '英语':'150'})
heindex.add_info({'理综':'30'})
heindex.del_info('艺术')
heindex.mod_info('理综','300')
heindex.see_info('理综')
heindex.see_info('艺术')
