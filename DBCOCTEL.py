from abc import ABC, abstractmethod, ABCMeta
import sqlite3

#INTERFACES#
class Database(metaclass=ABCMeta):
    @abstractmethod
    def addCoctel(self):
        pass
    @abstractmethod
    def updateCoctel(self):
        pass
    @abstractmethod
    def deleteCoctel(self):
        pass
    @abstractmethod
    def readCoctel(self):
        pass
    @abstractmethod
    def readCocteles(self):
        pass

class DB_Coctel(Database):
    def __init__(self):
        self.con = sqlite3.connect("coctel.db")
        self.cursor = self.con.cursor()

    def Close(self):
        self.con.close()
    def Commit(self):
        self.con.commit()

    def create_table(self):
       query = ('''
        CREATE TABLE IF NOT EXISTS COCTELES(
            id number primary key not null,
            name varchar(500) not null,
            category varchar(500) not null,
            alcohol varchar(500) not null,
            instructions varchar(500) not null,
            imagen varchar(500) not null,
            ingredients varchar(900) not null
        );
       ''')
       self.cursor.execute(query)
       self.con.commit()

    def addCoctel(self, id,name,category,alcohol,instructions,imagen,ingredients):
        try:
            query = f'''
                INSERT INTO COCTELES(id,name,category,alcohol,instructions,imagen,ingredients)
                values({id},"{name}","{category}","{alcohol}","{instructions}","{imagen}","{ingredients}");
            '''
            self.cursor.execute(query)
            self.con.commit()
            return "EXITO"
        
        except : return "ERROR"
    
    def updateCoctel(self, id, name, category,alcohol,instructions,imagen,ingredients):
        try:
            query = f'''
                UPDATE COCTELES SET name = "{name}" ,category = "{category}",alcohol = "{alcohol}",
                instructions = "{instructions}",imagen = "{imagen}",ingredients = "{ingredients}" 
                WHERE id = {id};
            '''
            self.cursor.execute(query)
            self.con.commit()
            return "EXITO"
        except : return "ERROR"
    
    def deleteCoctel(self, name):
        try:
            query = f'''
                delete from COCTELES where name = "{name}";
            '''
            self.cursor.execute(query)
            self.con.commit()
            return "EXITO"
        except : return "ERROR"
    
    def readCoctel(self, name):
        try:
            query = f'''
                select * from COCTELES where name = "{name}";
            '''
            return self.cursor.execute(query).fetchone()
        except : return "ERROR"
            
        
    def readCocteles(self):
        try:
            query = f'''
                select * from COCTELES;
            '''
            return self.cursor.execute(query).fetchall()
        except : return "ERROR"
    
if __name__ == "__main__":
    pass
    
    #bd = DB_Coctel()
    #bd.create_table()
    #bd.addCoctel(11007,"Margarita","Ordinary Drink","Alcoholic","Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass","https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg",['Tequila','Triple sec','LIme juice','Salt'])
    #print(bd.readCocteles())
    #ID 15328
    #bd.addCoctel(18328,"Zorro",	"Coffee / Tea","Alcoholic","add all and pour black coffee and add whipped cream on top","https://www.thecocktaild…ink/kvvd4z1485621283.jpg",['Sambuca','Baileys irish cream','White Creme de Menthe'])
    #print(bd.readCocteles())
    #bd.addCoctel(17208,"Rose","Ordinary Drink","Alcoholic","Shake together in a cocktail shaker, then strain into chilled glass. Garnish and serve.","https://www.thecocktaildb.com/images/media/drink/8kxbvq1504371462.jpg",['Dry Vermouth','Gin','Lemon juice','Grenadine','Powdered sugar'])
    #print(bd.readCocteles())
    #bd.updateCoctel(15328,"Zorro",	"Coffee / Tea","Alcoholic","add all and pour black coffee and add whipped cream on top","https://www.thecocktaild…ink/kvvd4z1485621283.jpg",['Sambuca','Baileys irish cream','White Creme de Menthe'])
    #print(bd.readCocteles())
    #bd.deleteCoctel("Rose")
    #print(bd.readCocteles())
    #print(bd.readCoctel("Margarita"))
    #print(bd.readCocteles())