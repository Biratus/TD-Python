import sqlite3
from Activites import Activites
import json

"""conn = sqlite3.connect('installations.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS installations")
c.execute('''CREATE TABLE installations
             (InsNumeroInstall integer,ComLib text,ComInsee integer,InsCodePostal integer)''')
c.execute("DROP TABLE IF EXISTS equipements")
c.execute('''CREATE TABLE equipements
             (ComInsee integer,ComLib text,InsNumeroInstall integer,EquipementId integer,EquNom text)''')
c.execute("DROP TABLE IF EXISTS activites")
c.execute('''CREATE TABLE activites
             (ComInsee integer,ComLib text,EquipementId integer,ActCode integer)''')

conn.commit()
conn.close()
def initBDEquipCSV(filepath) :
	f=open(filepath,'r');
	while(true) :
		l=readline()
		if(l==None) break;
		else :
			pass"""
#Exemple code JSON
json_file = "BD/Activites.json"

file_data = json.load(open(json_file))
for item in file_data["data"]:
	inst=Activites(item["ComInsee"],item["ComLib"],item["EquipementId"],item["ActCode"])
	print (inst)
	