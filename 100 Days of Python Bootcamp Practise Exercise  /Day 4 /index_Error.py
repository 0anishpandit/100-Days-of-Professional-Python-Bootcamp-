#when we try to use something that is out of index of list then it gives the index error as you can see in the example

cities_in_nepal = ["Kathmandu", "Pokhara", "Bharatpur", "Lalitpur", "Birgunj", "Biratnagar", "Dhangadhi", "Ghorahi", "Itahari", "Hetauda", "Janakpur", "Butwal", "Tulsipur", "Dharan", "Nepalgunj", "Kalaiya", "Jitpursimara", "Birendranagar", "Budhanilkantha", "Tarakeshwar", "Gokarneshwar", "Chandragiri", "Tokha", "Kageshwori-Manohara", "Mechinagar", "Bhimdatta", "Sundar Haraincha", "Madhyapur Thimi", "Mahalaxmi", "Birtamod", "Nagarjun", "Damak", "Triyuga", "Godawari", "Kohalpur", "Tikapur", "Siraha", "Bhaktapur", "Banepa", "Rajbiraj", "Lahan", "Panauti", "Kirtipur", "Gaur", "Dipayal-Silgadhi", "Inaruwa", "Ramgram", "Jaleswar", "Baglung", "Tansen"
 ]

print(len(cities_in_nepal))
print(cities_in_nepal[49])
# print(cities_in_nepal[50])  #this will give the index error , remove comment to check it.

#nested_list

SAARC_country = ["Nepal" , "India" , "Bangladesh" , "Pakistan" , "Afghanistan" , "Bhutan" , "The Maldives" , "Srilanks"]
world_countries = ["Nepal" , "India" , "China" , "USA" , "Europe" , "London" , "Paris" , "Quwat" , "Dubai" , "Bhutan" , "Ethopia" , "Nigeria" , "Rawanda" , "Kenia"]

nested_list = [SAARC_country , world_countries]

print(nested_list)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][1])