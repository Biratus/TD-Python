class Installations :
	def __init__ (self,InsNumeroInstall,ComLib,ComInsee,InsCodePostal) :
		self.InsNumeroInstall=InsNumeroInstall;
		self.ComLib=ComLib;
		self.ComInsee=ComInsee;
		self.InsCodePostal=InsCodePostal;
	def getInsNumeroInstall(self) :
		return self.InsNumeroInstall
	def getComLib(self) :
		return self.ComLib
	def getComInsee(self) :
		return self.ComInsee
	def getInsCodePostal(self) :
		return self.InsCodePostal;
	def setInsNumeroInstall(self,c) :
		self.InsNumeroInstall=c
	def setComLib(self,c) :
		self.ComLib=c
	def setComInsee(self,c) :
		self.ComInsee=c
	def setInsCodePostal(self,c) :
		self.InsCodePostal=c
	def SQLInsert(self,dbName) :
		return "INSERT INTO {0} VALUES ('{1}','{2}','{3}','{4}')".format(dbName,self.InsNumeroInstall,self.ComLib,self.ComInsee,self.InsCodePostal)

def loadJsonFile() :
	json_file = "BD/Installations.json"
	tab=[]
	file_data = json.load(open(json_file))
	for item in file_data["data"]:
		tab.append(Installations(item["InsNumeroInstall"],item["ComLib"],item["ComInsee"],item["InsCodePostal"]))
	return tab
	