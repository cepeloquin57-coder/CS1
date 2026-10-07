print(f"---Question 1---\n Favorite Numbers")
favorite_numbers = {
                    'Amanda':7,
                    'Beatrice':12,
                    'Catherine':13,
                    'Deirdre':3,
                    'Eleanora':5
                    }
for name in favorite_numbers.keys():
    print(name, favorite_numbers[name])
print(f"---Question 2---\n Rivers")
rivers = {
    'nile':'egypt',
    'yangtze':'china',
    'amazon':'brazil'
    }
for river in rivers.keys():
    print(f"The {river.title()} runs through {rivers[river].title()}.")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
print(f"---Question 3---\n Pets")
fluffy = {
        'species':'hamster',
        'owner':'Frederica'
          }
lady = {
    'species':'snake',
    'owner':'Georgiana'
}
pets=[fluffy,lady]
for pet in range(len(pets)):
    for characteristic in pets[pet].keys():
        print(f"{characteristic}: {pets[pet][characteristic]}")
print(f'{pets[0]}')
print(f"---Question 4---\n Favorite Places")
favorite_places = {'Harriet':'library',
                   'Iphigenia':['cafeteria','laboratory'],
                   "Jeanne":["gym", 'dorm', 'library']
                   }
for name in favorite_places.keys():
    print(name,':', favorite_places[name])
print(f"---Question 5---\n Movie Ratings")
movie_ratings = {
            "The Princess Bride":8,
            "The Handmaiden":8,
            "Titanic":7
            }
for movie in movie_ratings.keys():
    if movie_ratings[movie]>=8:
        print(movie,':', movie_ratings[movie])
print(f"---Question 6---\n Restaurant Menu")
menu ={
    "Fettuccine Alfredo":24.95,
    "Tortellini Carbonara":26.99,
    "Risotto alla Milanese":25.95,
    "Arancini":15.99,
    "Tiramisu":16.95
    }
for food in menu.keys():
    print(food,':', menu[food])
print(f"\n")
menu['Pizza Margherita'] = 23.95
menu["Arancini"] = 17.99
for food in menu.keys():
    print(food,':', menu[food])
print(f"---Question 7---\n Cities")
cities = {
    'Paris':{
        'country': 'France',
        'population': '2.04 million',
        'fun fact': "The city's motto is 'Fluctuat nec mergitur', which means 'Tossed upon the waves, but never sunk'."
        },
    'Boston':{
        'country':'USA',
        'population':'0.65 million',
        'fun fact': 'Boston is the most populous city in Massachusetts'
        },
    'Shanghai':{
        'country':'China',
        'population': '30.05 million',
        'fun fact':'Shanghai is the fifth most populous city in the world.'
        }
    }