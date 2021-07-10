


import random
import pickle

file = "file.pkl"
with open(file, 'rb') as f:
    dictionary = pickle.load(f)


nice_movies = []
for i, k in dictionary.items():
    if(float(dictionary[i]) >= 7.0):
        nice_movies.append(float(dictionary[i]))

try1 = []
for i, k in dictionary.items():  
    for z in range(len(nice_movies)):
        if k == str(nice_movies[z]):
            try1.append(i)

new_dict = {}
for i in range(len(try1)):
    if(try1[i] not in new_dict):
        new_dict[try1[i]] = 1

# check = random.randint(0,2)
# blashphemy = try1[check]
# movie = blashphemy
#movie = dictionary.get(str(highest))
best_movies_with_specified_rating = new_dict.keys()
dis = list(best_movies_with_specified_rating)

xd = True
while xd:
    vs = input("Movie or No ")
    if vs == 'No':
        xd = False
    
    bruhfus = random.randint(0, len(dis)-1)
    print("The movie you gonna watch bro: " + dis[bruhfus])

#r = list(best_movies_with_specified_rating)
# nabiha = []
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}

# for i in range(len(r)):
#     website = "https://www.google.com/search?sxsrf=ALeKk005crlz6J-UScR5SsuwFRyOHBAcmg%3A1596341753508&source=hp&ei=-T0mX8ilHIvktQWYjLboCQ&q=" + r[i] + "&oq=Midsommar&gs_lcp=CgZwc3ktYWIQAzILCC4QsQMQkQIQkwIyCggAELEDEBQQhwIyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIICAAQsQMQgwEyBQgAELEDMgUIABCxAzoHCCMQ6gIQJzoHCC4Q6gIQJzoNCC4QxwEQowIQJxCTAjoECC4QJzoECCMQJzoFCAAQkQI6CwguELEDEMcBEKMCOgUILhCRAjoFCC4QsQM6AggAOggILhCxAxCRAjoKCC4QsQMQFBCHAjoICC4QsQMQgwE6AgguOggILhDHARCvAVDdGFiCJGDXJGgBcAB4AIABeYgBxgWSAQM4LjGYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwiIhp-51PvqAhULcq0KHRiGDZ0Q4dUDCAk&uact=5"
#     req = Request(website, headers=headers)
#     page = urlopen(req)
#     soup = BeautifulSoup(page, 'html.parser')
#     for item in soup.select(".kno-rdesc span"):
#         test1 = item.get_text().split()
#         if isinstance(test1, list):
#             nabiha.append(test1)
            
# #print("The movie you watching tonight bro " + movie)


# #r <-- Contains the movies
# #nabiha <-- Contains the description of the movies

# bruh_really = {}

# for v in range(len(nabiha)):
#     bruh_really[r[v]] = nabiha[v]


# print(bruh_really) 






