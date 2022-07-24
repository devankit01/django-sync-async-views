from django.http import HttpResponse
import time, asyncio
from movies.models import Movie
from stories.models import Story
from asgiref.sync import sync_to_async
from django.shortcuts import render
import requests, time, aiohttp

# helper funcs

def get_movies():
    print('prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all the movies!')

def get_stories():
    print('prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all the stories!')

@sync_to_async
def get_movies_async():
    print('prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all the movies!')

@sync_to_async
def get_stories_async():
    print('prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all the stories!')

# views

def home_view(request):
    return HttpResponse('Hello world')

def main_view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time()-start_time)
    print('total: ', total)
    return HttpResponse('sync')
    # total:  7.0053699016571045

async def main_view_async(request):
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_movies_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total: ', total)
    return HttpResponse('async')

    # total:  5.002896070480347

from .utils import fetch


async def async_view_v2(request):
    start_time = time.time()
    
    url_list  = [ 'https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']


    async with aiohttp.ClientSession() as client:
        tasks = []

        for url in url_list:
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)
        results =  await asyncio.gather(*tasks)

    total = time.time() - start_time

    # Total Time
    print("Async : ", total)
    return render(request, 'home.html',{'data1' : results[0], 'data2': results[1]})


def sync_view_v2(request):
    start_time = time.time()
    data =  []
    url_list  = [ 'https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']
    for url in url_list:

        data.append(requests.get(url).json())
    total = time.time() - start_time

    # Total Time
    print("Sync : " , total)
    return render(request, 'home.html',{'data1' : data[0], 'data2': data[1]})