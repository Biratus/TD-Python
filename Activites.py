class Activites :
	def __init__(self,ComInsee,ComLib,EquipementId,ActCode) :
		self.ComInsee=ComInsee;
		self.ComLib=ComLib;
		self.EquipementId=EquipementId;
		self.ActCode=ActCode;
	def getComInsee(self) :
		return self.ComInsee;
	def getComLib(self) :
		return self.ComLib;
	def getEquipementId(self) :
		return self.EquipementId;
	def getActCode(self) :
		return self.ActCode;
	def setComInsee(self,c) :
		self.ComInsee=c;
	def setComLib(self,c) :
		self.ComLib=c;
	def setEquipementId(self,c) :
		self.EquipementId=c;
	def setActCode(self,c) :
		self.ActCode=c;
