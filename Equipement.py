class Equipement :
	def __init__ (self,ComInsee,ComLib,InsNumeroInstall,EquipementId,EquNom) :
		self.ComInsee=ComInsee;
		self.ComLib=ComLib;
		self.InsNumeroInstall=InsNumeroInstall;
		self.EquipementId=EquipementId;
		self.EquNom=EquNom;
	def getComInsee(self) :
		return ComInsee;
	def getComLib(self) :
		return ComLib;
	def getInsNumeroInstall(self) :
		return InsNumeroInstall;
	def getEquipementId (self) :
		return EquipementId;
	def getEquNom(self) :
		return EquNom;
	def setComInsee(self,c) :
		self.ComInsee=c;
	def setComLib(self,c) :
		self.ComLib=c;
	def setInsNumeroInstall(self,c) :
		self.InsNumeroInstall=c;
	def setEquipementId (self,c) :
		self.EquipementId=c;
	def setEquNom(self,c) :
		self.EquNom=c;