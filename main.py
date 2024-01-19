import requests
import json
import pandas as pd

def call_API(foodName, apiKey):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={apiKey}&query={foodName}'
    r = requests.get(url)
    print(r.status_code)  # 200
    return r.json()


def call_API_2(foodName, apiKey):
    data = {"query" : foodName}
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={apiKey}'
    r = requests.post(url, json=data)
    print(r.status_code)  # 200
    return r.json()

food = input("Enter a food item: ")
ans = call_API_2(food, "Xie5HhhZC8t038z0mUi2Ae9zasyNfTiYFTxttouA")

#print(type(ans))

table = pd.DataFrame(ans['foods'])
foodNutrients = table.iloc[0]['foodNutrients']
print(table.iloc[0]['description'])
for i in foodNutrients:
  print(i['nutrientName'], i['value'])
#print(foodNutrients[0])
#protein_value = table.iloc[0]['foodNutrients'][0]['nutrientValue']
#print("Protein: ", protein_value)



#print(ans)

#print(pd.read_json(ans))
#for i in ans['foods'][0]:
#    print(i)
    
    #if str(i) == 'foodNutrients':
    #    for j in i:
    #        print(j)
        
#        print(i['nutrientName'] + ": " + i['value'] + i['unitName'])
#        break
