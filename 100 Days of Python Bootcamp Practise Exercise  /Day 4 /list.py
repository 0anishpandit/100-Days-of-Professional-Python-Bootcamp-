#lsit is something that stores the sma e group of items
#syntax of list
# list_name = [" " , " " , " " ]
cities_of_nepal = ["dharan" , "Itahari" , "Inaruwa"]
print( cities_of_nepal[0 : 2])  #slicing the list element
cities_of_nepal[1] = "Kathmandu"
print( cities_of_nepal[1])

cities_of_nepal.append("Pokhara")  #append will add the item to the end of the list

cities_of_nepal.extend(["Jhapa" ,"Damak" , "sundarharichha"])  #add another list to the list
print(cities_of_nepal)

