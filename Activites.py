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
	def SQLInsert(self,dbName) :
		return "INSERT INTO {0} VALUES ('{1}','{2}','{3}','{4}')".format(dbName,self.ComInsee,self.ComLib,self.EquipementId,self.ActCode)
def loadJsonFile() :
	json_file = "BD/Activites.json"
	tab=[]
	file_data = json.load(open(json_file))
	for item in file_data["data"]:
		tab.append(Activites(item["ComInsee"],item["ComLib"],item["EquipementId"],item["ActCode"]))
	return tab
	