import sqlite3

conn = sqlite3.connect('installations.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS installations")
c.execute('''CREATE TABLE installations
             (Insnom text,InsNumeroInstall integer,ComLib text,ComInsee integer,InsCodePostal integer)''')
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
			pass
#Exemple code JSON
json_file = "data.json"

import json

file_data = open(json_file).read()
json_data = json.reads(file_data)

for item in json_data["data"]:
	print(item)