import unittest
from unittest.mock import MagicMock
from CLASSCOCTEL import *
from DBCOCTEL import *
import os

class test_DB(unittest.TestCase):
#test de crear la BD
 
    def setUp(self):
        self.buscar = GET_API()
        self.db = DB_Coctel()
        self.db.create_table()
        self.db.addCoctel(12362,"Tequila Fizz","Ordinary Drink","Alcoholic","Shake all ingredients (except ginger ale) with ice and strain into a collins glass over ice cubes. Fill with ginger ale, stir, and serve.","https://www.thecocktaildb.com/images/media/drink/2bcase1504889637.jpg",['Tequila','Lemon juice','Grenadine','Egg white','Ginger ale'])
        print(self.db)
        
    #def tearDown(self):
    #    self.db.Close()
    #    os.remove("coctel.db")
        
    #def testInsert(self):
    #    coctel = [
    #    {
    #    "entrada":{
    #            "id" : "11007", "name" : "Margarita", "category" : "Ordinary Drink", "alcohol": "Alcoholic",
    #            "instructions":"Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass",
    #            "imagen": "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg" ,
    #            "ingredients": ['Tequila','Triple sec','LIme juice','Salt']        
    #    },
    #    "salida":"EXITO"
    #    },
    #    {
    #    "entrada":{
    #            "id":"17141", "name" : "smut","category": "Punch/Party Drink", "alcohol": "ALcoholic",
    #            "instructions":"Throw it all together and serve real cold.",
    #            "imagen": "https://www.thecocktaildb.com/images/media/drink/rx8k8e1504365812.jpg",
    #            "ingredients":['Red wine','Peach schnapps','Pepsi Cola','Orange juice']
    #    },
    #    "salida":"EXITO"
    #    }
    #    ]
        
        #test para insertar a la BD
    #    for coc in coctel:
    #        a = self.db.addCoctel(**coc.get("entrada"))
    #        self.assertEqual(coc.get("salida"), a)
            
        
    
    # def testaddCoctel(self):
    #     coctel = [
    #     {
    #     "entrada":"Margarita",
    #     "salida":"EXITO"
    #     },
    #     {
    #     "entrada":"smut",
    #     "salida":"EXITO"
    #     }
    #     ]
        
    #     #integracion api-clase con bd insert
    #     for coc in coctel:
    #         #a = self.db.addCoctel(**coc.get("entrada"))
    #         #self.assertEqual(coc.get("salida"), a)
    #         a = self.buscar.get_coctel(coc.get("entrada"))
    #         res = self.db.addCoctel(**a.get_data())
    #         self.assertEqual(coc.get("salida"),res)

    #TEST UPDATE DB
    #def testUpdate(self):
    #    coctel=[
    #    {
    #    "entrada":{
    #            "id" : "11800", "name" : "Margarita", "category" : "Ordinary Drink", "alcohol": "Alcoholic",
    #            "instructions":"Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass",
    #            "imagen": "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg" ,
    #            "ingredients": ['Tequila','Triple sec','LIme juice','Salt']        
    #    },
    #    "salida":"EXITO"
    #    },
    #    {
    #    "entrada":{
    #            "id":"18963", "name" : "smutie","category": "Party Drink", "alcohol": "ALcoholic",
    #            "instructions":"Throw it all together and serve real cold.",
    #            "imagen": "https://www.thecocktaildb.com/images/media/drink/rx8k8e1504365812.jpg",
    #            "ingredients":['Tequila','Peach schnapps','Pepsi Cola','Orange juice']
    #    },
    #    "salida":"EXITO"
    #    }
    #    ]
        
    #    for coc in coctel:
    #        a = self.db.updateCoctel(**coc.get("entrada"))
    #        self.assertEqual(coc.get("salida"), a)
        
        
    #def testDelete(self):
    #    coctel=[
    #    {
    #    "entrada":{
    #            "name" : "Margarita"     
    #   },
    #    "salida":"EXITO"
    #    },
    #    {
    #   "entrada":{
    #            "name" : "smutie"
    #    },
    #    "salida":"EXITO"
    #    }
    #    ]
        
    #    for coc in coctel:
    #        a=self.db.deleteCoctel(**coc.get("entrada"))
    #        self.assertEqual(coc.get("salida"),a)
    
 
    # def testReadCocteles(self):
    #    coctel=[
    #        {"entrada" :{"id":"12362","name":"Tequila Fizz","category":"Ordinary Drink","alcohol":"Alcoholic","instructions":"Shake all ingredients (except ginger ale) with ice and strain into a collins glass over ice cubes. Fill with ginger ale, stir, and serve.",
    #                       	"imagen":"https://www.thecocktaildb.com/images/media/drink/2bcase1504889637.jpg","ingredients":['Tequila','Lemon juice','Grenadine','Egg white','Ginger ale']
    #        },
    #         "salida": "EXITO"}
    #    ]
        
    #    for coc in coctel:
    #        a=self.db.readCocteles(**coc.get("entrada"))
    #        self.assertEqual(coc.get("salida"),a)
            
    #        print(a)
    
    
    def testReadCoctel(self):
        coctel=[
        {
        "entrada":{
                 "name" : "Tequila Frizz"       
        },
        "salida":"EXITO"
        }
        ]
        for coc in coctel:
            a=self.db.readCoctel(**coc.get("entrada"))
            self.assertEqual(coc.get("salida"),a)
            print(a)
        
        

#        
if __name__ == '__main__':
    unittest.main()    