class Installations :
	def __init__ (self,Insnom,InsNumeroInstall,ComLib,ComInsee,InsCodePostal) :
		self.Insnom=Insnom;
		self.InsNumeroInstall=InsNumeroInstall;
		self.ComLib=ComLib;
		self.ComInsee=ComInsee;
		self.InsCodePostal=InsCodePostal;
		self.InsLieuDit=InsLieuDit;
	def getInsNom(self) :
		return self.InsNom;
	def getInsNumeroInstall(self) :
		return self.InsNumeroInstall;
	def getComLib(self) :
		return self.ComLib;
	def getComInsee(self) :
		return self.ComInsee;
	def getInsCodePostal(self) :
		return self.InsCodePostal;
	def getInsLieuDit(self) :
		return self.InsLieuDit;
	def setInsNom(self,c) :
		self.InsNom=c;
	def setInsNumeroInstall(self,c) :
		self.InsNumeroInstall=c;
	def setComLib(self,c) :
		self.ComLib=c;
	def setComInsee(self,c) :
		self.ComInsee=c;
	def setInsCodePostal(self,c) :
		self.InsCodePostal=c;
	def setInsLieuDit(self,c) :
		self.InsLieuDit=c;