from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
import random
import pickle
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib
import json
from requests.exceptions import MissingSchema, InvalidURL



def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio\home.html', {'projects': projects})


def programs_all1(request):
    return render(request, 'portfolio\programmer.html')


def resume(request):
    return render(request,'portfolio\lol.html')
    #return HttpResponse("Print work?")


def program(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'file.pkl')
    file = file_path
    with open(file, 'rb') as f:
        dictionary = pickle.load(f)


    nice_movies = []
    for i, k in dictionary.items():
        if(float(dictionary[i]) >= 6.0):
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


    best_movies_with_specified_rating = new_dict.keys()
    dis = list(best_movies_with_specified_rating)
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    # for movie in dis:
    #     url = "https://www.google.com/search?ei=38BBX4azMIKwtQXyzISAAg&q=One+CutoftheDead&oq="+ movie + "&gs_lcp=CgZwc3ktYWIQDDIHCC4QDRCTAjIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDToHCAAQRxCwA1DkWljkWmD8ZGgCcAB4AIABMIgBMJIBATGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjGnpuKkbDrAhUCWK0KHXImASAQ4dUDCAw"
    #     req = Request(url, headers=headers)
    #     page = urlopen(req)
    #     soup = BeautifulSoup(page, 'html.parser')

    # xd = True
    # while xd:
    #     vs = input("Movie or No ")
    #     if vs == 'No':
    #         xd = False
    
    bruhfus = random.randint(0, len(dis)-1)
    #print("The movie you gonna watch bro: " + dis[bruhfus])
    movie1 = dis[bruhfus]

    nabiha = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(nabiha, 'totally_new.pkl')
    file2 = file_path
    with open(file2, "rb") as f:
        z = pickle.load(f)
    
    for_the_movie = z[movie1]


    
    url = "http://www.omdbapi.com/?t=" + str(for_the_movie) + "&apikey=2d514876"
    response = urllib.request.urlopen(url)
    if response != None:
    
        data = json.loads(response.read())
        
        print(data)

        nz = data["Year"]

        zn = data['Plot']

    return render(request, 'portfolio\programmer.html', {'movie':for_the_movie, 'Year':nz, 'Plot':zn})


