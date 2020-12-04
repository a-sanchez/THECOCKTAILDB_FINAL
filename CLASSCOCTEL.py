from abc import ABC,abstractmethod, ABCMeta
import requests
import json
import unittest

class Coctel():
    def __init__(self,id,name,Category,alcohol,instructions,imagen,ingredients):
        self.id = id
        self.name = name
        self.Category = Category
        self.alcohol = alcohol
        self.instructions = instructions
        self.imagen = imagen
        self.ingredients = ingredients
        
    def get_data(self):
        data = {
            "id" : self.id,
            "name": self.name,
            "category" : self.Category,
            "alcohol" : self.alcohol,
            "instructions" : self.instructions,
            "imagen" : self.imagen,
            "ingredients" : self.ingredients
        }
        return data
    
    def __str__(self):
        r = ""
        r = r + f"id : {self.id}"
        r += f"\nname: {self.name}"
        r += f"\nCategory : {self.Category}"
        r += f"\nalcohol : {self.alcohol}"
        r += f"\ninstructions : {self.instructions}"
        r += f"\nimagen : {self.imagen}"
        r += f"\ningredients : {self.ingredients}"
        return r
    
class APICOCTEL(metaclass = ABCMeta):
    @abstractmethod
    def get_coctel(self):
        pass
    
class GET_API(APICOCTEL):
    def __init__(self):
        self.endpoint = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" 
        
        
    def get_coctel(self,name):
        coctel = requests.get(self.endpoint + name) 
        coctel = json.loads(coctel.text)
        c = coctel["drinks"][0]
        id = c["idDrink"]
        name = c["strDrink"]
        tag = c["strCategory"]
        alcohol = c["strAlcoholic"]
        instructions = c["strInstructions"]
        img = c["strDrinkThumb"]
        ing = []
        lista = "strIngredient" 
        for i in range(1,15):
            if c[f"{lista}{i}"] != None:
                ing.append(c[f"{lista}{i}"])
        new_coctel = Coctel(id,name,tag,alcohol,instructions,img,ing)
        return new_coctel

def build_coctel(api,coctel):
    return api.get_coctel(coctel)

if __name__ == "__main__":
    p = GET_API()
    c = "margarita"
    print(build_coctel(p,c))


