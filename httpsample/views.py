from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.


def get(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts',
                            verify=False)
    posts = response.json()
    return render(request, 'httpsample/index.html', {'post_list': posts})


def add(request):
    body = {"title": "test title"}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             data=body,
                             verify=False)
    return HttpResponse(response)


def edit(request):
    body = {"id": 1, "title": "test update title"}
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1',
                            data=body,
                            verify=False)
    return HttpResponse(response)


def delete(request):
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1',
                               verify=False)
    return HttpResponse(response)