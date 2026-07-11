"""
Dictionary =>
		
		Dictionary is an unordered collection of key-value pairs enclosed with{}
		it is mutable

		eg:-		color = {'Green': 10,'Black': 5, 'White':15}


		=> Extract keys and value
			   Extracting keys :-
				      color.keys()
				      //result=dict_keys(['Green','Black','White'])

			   Extracting values
				      color.values()
				      //result=dict_values([10,5,15])

		=> Modifying a Dictionary
			  => Adding a new Element
				    color['Red']= 12
				    color
			  => changing an existing element
				    color['Green'] = 100
				    color
			  => update the dictionary
				    color1 ={'red':10, 'black':20, 'black':11}
				    color2= {'white':25, 'grey':30, 'red':17}
				    color1.update(color2)
				    print(color1)
				    {'red'=17, 'black'=11, 'white'=25, 'grey'=30} // color1 update

			  => pop out the specific key-value pair
				     color1.pop('red')
				     """
#Dictionary creations
#Create a dictionary called inventory for a grocery store where the keys are fruit names and values are their prices
grocery = {
           "apple": 250,
           "orange": 310,
           "Kiwi": 260,
           "litchi": 320,
           "grapes": 370,
           "watermelon":370
}
print(grocery)

    
# Access  
print(grocery.values())
print(grocery.keys())
print(grocery["apple"])
print(grocery["litchi"])
price = grocery.get("mango","Fruit not found")
print(price)


#Modify
grocery["cherry"] = 280 #add new element
grocery["apple"] = 500 


grocery.pop("apple")#pop

for fruit, price in grocery.items():
    print(f"The price of {fruit} is {price}")
    
demand = input("what you wanna buy from our shop: ")
h= grocery.get(demand,"deman is not found ")
print("your toral bill for 1kg" ,demand, "is",h)
